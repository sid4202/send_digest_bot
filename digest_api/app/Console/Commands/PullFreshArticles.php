<?php

namespace App\Console\Commands;

use Illuminate\Console\Command;
use App\Services\RiaParser;
use App\Services\RbkParser;
use App\Services\PrimeParser;
use App\Models\Article;

class PullFreshArticles extends Command
{
    protected $signature = 'app:pull-fresh-articles';
    protected $description = 'Pull and parse all the fresh pieces of news';

    public function handle()
    {
        $parsers = [
            RiaParser::class,
            RbkParser::class,
            PrimeParser::class,
        ];

        foreach ($parsers as $parser)
        {
            $parser = new $parser();
            $parser->getArticles();
        }
    }
}
