<?php

namespace App;

abstract class Parser
{
    abstract protected function setCacheKey(): void;
    abstract protected function setSearchQueries(): void;
    abstract protected function getLinks(): void;
    abstract protected function getArticleTextsAndTitles(): array;
    abstract protected function parseArticle(string $url): array;
    abstract public function getArticles(): array;
    
}
