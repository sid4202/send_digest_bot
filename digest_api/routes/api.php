<?php 

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\ParseArticleController;


Route::any('ping', fn() => 'pong')->name('ping');
Route::get('parseArticle', [ParseArticleController::class, 'getLatestArticle'])->name('parseArticle');
