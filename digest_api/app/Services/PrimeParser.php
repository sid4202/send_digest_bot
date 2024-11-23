<?php

namespace App\Services;

use App\Parser;
use PHPHtmlParser\Dom;
use Illuminate\Support\Facades\Cache;
use PHPHtmlParser\Options;
use App\Models\Article;




class PrimeParser extends Parser
{
    private string $cacheKey;
    private array $searchQueries;

    protected function setCacheKey(): void
    {
        $this->cacheKey = 'prime';
    }

    protected function setSearchQueries(): void
    {
        $this->searchQueries = config('app.search_query.prime');

    }
    protected function getLinks(): void 
    {
        $this->setCacheKey();
        $this->setSearchQueries();
        $linksToSave = [];

        foreach ($this->searchQueries as $query) {
            $html = file_get_contents(filename: 'https://1prime.ru/search/?query='.toAsciiHex($query));

            $dom = new Dom();
            $dom->loadStr($html);

            $linksList = [];

            $a = $dom->find('a');
            foreach($a as $link) {
                if ($link->class == 'list-item__title color-font-hover-only') {
                    $linksList[] = 'https://1prime.ru'.$link->href;
                }
            }

            $linksToSave[$query] = $linksList;
            sleep(rand(5, 10));
            
        }
        var_dump($linksToSave);
        $linksToSaveJson = json_encode($linksToSave);
        if (!Cache::has($this->cacheKey)) {
            Cache::set($this->cacheKey, $linksToSaveJson);
        } else {
            Cache::put($this->cacheKey, $linksToSaveJson);
        }
        
    }

    protected function getArticleTextsAndTitles(): void
    {  
        echo "PARSING STARTS"."\n"; 
        $links = json_decode(Cache::get($this->cacheKey), true);

        $dom = new Dom();

        foreach ($this->searchQueries as $query) {
            foreach ($links[$query] as $link) {
                var_dump($link);
                var_dump($links[$query]);

                sleep(rand(5, 10));
                $article = $this->parseArticle($link);
                Article::query()->create([
                    'text' => $article['text'],
                    'source' => $article['source'],
                    'title' => $article['title']
                ]);
            }
        }
    }

    protected function parseArticle(string $url): array
        {  
            echo "PARSING ARTICLE"."\n"; 
            $dom = new Dom();

            $html = file_get_contents($url);
            
            $dom->loadStr($html);

            $title = $dom->find('title')[0]->text();
            $div = $dom->find('div');
            $articleText = '';
                
            foreach ($div as $block) {
                if ($block->class == 'article__text ') {
                    $articleText .= $block->text."\n";
                }
            }
            $article = [
                    'source' => $url,
                    'text' => $articleText,
                    'title' => $title
            ];
            var_dump($article);
            return $article;
    }
    public function getArticles(): void
    {
        $this->getLinks();
        $this->getArticleTextsAndTitles();
    }
}