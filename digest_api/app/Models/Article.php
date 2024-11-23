<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\HasOne;

/**
 * @property string $text
 * @property string $source
 * @property string $title
 * @property int $id
 */

class Article extends Model
{
    public const UPDATED_AT = null;
    public const CREATED_AT = null;

    protected $table = 'article';

    protected $fillable = [
        'text',
        'source',
        'title'
    ];

    public function articleFilter(): HasOne
    {   
        return $this->hasOne(ArticleFilter::class);
    }

    public function getFilter() {
        if ($this->articleFilter() === null) {
            return ArticleFilter::query()->create([
                'article_id' => $this->id,
                'accepted' => null
            ]);
        } else {
            return $this->articleFilter();
        }
    }
}