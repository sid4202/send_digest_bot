<?php

namespace App;
use Illuminate\Support\Facades\Cache;


abstract class Parser
{

    abstract protected function setCacheKey(): void;
    abstract protected function setSearchQueries(): void;
    abstract protected function getLinks(): void;
    abstract protected function getArticleTextsAndTitles(): void;
    abstract protected function parseArticle(string $url): array;
    abstract public function getArticles(): void;
    
}
