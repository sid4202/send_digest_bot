<?php

namespace App\Console\Commands;

use App\Models\Article;
use App\Models\ArticleFilter;

use Illuminate\Console\Command;

class SendArticlesToCheck extends Command
{
    protected $signature = 'app:send-articles-to-check';

    protected $description = 'Command description';

    public function handle()
    {
        $articles = Article::all();

        foreach ($articles as $article) {
            $filter = $article->getFilter();

            if ($filter->accepted === null)
                {
                    
                }
        }
    }
}
