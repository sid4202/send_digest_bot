<?php

namespace App\Services;

use App\Parser;
use PHPHtmlParser\Dom;
use Illuminate\Support\Facades\Cache;
use PHPHtmlParser\Options;



class RbkParser extends Parser
{
    private string $cacheKey;
    private array $searchQueries;

    protected function setCacheKey(): void
    {
        $this->cacheKey = 'rbk';
    }

    protected function setSearchQueries(): void
    {
        $this->searchQueries = [
            'rbk_realty' => 'https://realty.rbc.ru/?utm_source=topline',
            'rbk_invest' => 'https://www.rbc.ru/quote'
        ];
    }
    
    protected function getLinks(): void 
    {
        $this->setCacheKey();
        $this->setSearchQueries();
        $linksToSave = [];

        foreach ($this->searchQueries as $query) {
            $html = file_get_contents($query);
            $dom = new Dom();
            $dom->loadStr($html);
    
            $links = $dom->find('a');
    
            foreach ($links as $a)
            {
                if ($a->class === "news-feed__item js-visited js-news-feed-item js-yandex-counter") {
                    $linksToSave[] = $a->href;
                }
            }
    
            
        }
        var_dump($linksToSave);
        $linksToSaveJson = json_encode($linksToSave);
        if (!Cache::has($this->cacheKey)) {
            Cache::set($this->cacheKey, $linksToSaveJson);
        } else {
            Cache::put($this->cacheKey, $linksToSaveJson);
        }
        
    }
    protected function getArticleTextsAndTitles(): array
    {  
        $links = json_decode(Cache::get($this->cacheKey), true);

        $articles = [];
        $dom = new Dom();

        foreach ($links as $link) {
            var_dump($link);

            sleep(rand(5, 10));
            $articles[] = $this->parseArticle($link);
            var_dump($articles);
        }

        return $articles;
    }
    protected function parseArticle(string $url): array
    {  
        $dom = new Dom();

        $dom->loadFromUrl($url);
        
        $text = $dom->find('p')[2]->text;
        $title = $dom->find('title')[0]->text;

        $article = [
            'text' => $text,
            'title' => $title,
            'url' => $url
        ];

        return $article;
    }
    public function getArticles(): array
    {
        $this->getLinks();
        return $this->getArticleTextsAndTitles();
    }
}