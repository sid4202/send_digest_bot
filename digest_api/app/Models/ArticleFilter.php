<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class ArticleFilter extends Model
{
    public const UPDATED_AT = null;
    public const CREATED_AT = null;

    protected $table = 'article';

    protected $fillable = [
        'article_id',
        'accepted'
    ];
}
