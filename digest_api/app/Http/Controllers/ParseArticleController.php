<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use PHPHtmlParser\Dom;
use App\Services\RbkParser;
use PHPHtmlParser\Options;



class ParseArticleController extends Controller
{
    public function getLatestArticle(Request $request)
    {
        /*$parser = new RbkParser();

        var_dump($parser->getArticles());*/

        $html = file_get_contents('https://www.rbc.ru/quote/news/article/671b89a59a7947740ea82656');

        var_dump($html);
    }
}