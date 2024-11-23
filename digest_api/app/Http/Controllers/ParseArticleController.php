<?php

namespace App\Http\Controllers;

use App\Services\RiaParser;
use Illuminate\Http\Request;
use PHPHtmlParser\Dom;
use App\Services\RbkParser;
use App\Services\PrimeParser;
use PHPHtmlParser\Options;



class ParseArticleController extends Controller
{
    public function getLatestArticle(Request $request)
    {
        /*$parser = new RbkParser();

        var_dump($parser->getArticles());*/

        /*$html = file_get_contents('https://1prime.ru/20241025/ipoteka-852427695.html');
        //$html_utf8 = mb_convert_encoding($html, "utf-8", "windows-1251");
        $dom = new Dom();
        $dom->loadStr($html);

        //$p = $dom->find('a');
        //foreach($p as $div) {
           // $link = 'https://1prime.ru/20241025/ipoteka-852427695.html';
            /*if ($div->class == 'list-item__title color-font-hover-only') {
                $link = 'https://1prime.ru'.$div->href."\n";
            }*/
    
                /*$title = $dom->find('title')[0]->text();
                $div = $dom->find('div');
                $articleText = '';
    
                foreach ($div as $block) {

                    var_dump($block->class);
                    var_dump($block->text);
                    if ($block->class == 'article__text ') {
                        var_dump($block->text);
                        $articleText .= $block->text."\n";
                    }
                }
                $article = [
                    //'url' => $link,
                    'text' => $articleText,
                    'title' => $title
                ];
                var_dump($article);*/
        //$parser = new PrimeParser();
        //var_dump($parser->getArticles());

    }
}