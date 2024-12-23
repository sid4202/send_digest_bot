<?php

namespace App\Services;

use App\Parser;
use PHPHtmlParser\Dom;
use Illuminate\Support\Facades\Cache;
use App\Models\Article;


class RiaParser extends Parser
{
    private string $cacheKey;
    private array $searchQueries;

    protected function setCacheKey(): void
    {
        $this->cacheKey = 'ria';
    }

    protected function setSearchQueries(): void
    {
        $this->searchQueries = config('app.search_query.ria');
    }
    
    protected function getLinks(): void 
    {
        $this->setCacheKey();
        $this->setSearchQueries();
        $linksToSave = [];

        foreach ($this->searchQueries as $query) {
            $html = file_get_contents('https://ria.ru/search/?query='.toAsciiHex($query));

            $dom = new Dom();
            $dom->loadStr($html);
    
            $links = $dom->find("a.list-item__image");
            $linksList[] = $links[0]->href;
    
            /*foreach($links as $link)
            {
              $linksList[] = $link->href;
            }*/

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
        $links = json_decode(Cache::get($this->cacheKey), true);

        $dom = new Dom();

        foreach ($this->searchQueries as $query) {
            foreach ($links[$query] as $link) {
                var_dump($link);
                var_dump($links[$query]);

                sleep(rand(5, 10));
                $article = $this->parseArticle($link);
                var_dump(mb_convert_encoding(explode("\n", $article['text'])[0], 'utf-8'));

                Article::query()->create([
                    'text' => explode("\n", $article['text'])[0],
                    'source' => $article['source'],
                    'title' => $article['title']
                ]);
            }
        }
    }
    protected function parseArticle(string $url): array
    {  
        $dom = new Dom();

        try {
            $html = file_get_contents($url);
        } catch (NotFoundHttpException) {
            echo "Page not found"."\n";
            return [];
        }
        
        $dom->loadStr($html);
        
        $divs = $dom->find('div.article__text');
        $title = $dom->find('title')[0]->text;
        $text = "";
        
        foreach ($divs as $div) {
            $text .= $div->text."\n";
        }
        
        $article = [
                'title' => $title,
                'text' => $text,
                'source' => $url,
        ];

        return $article;
    }
    public function getArticles(): void
    {
        $this->getLinks();
        $this->getArticleTextsAndTitles();
    }
}