<?php 

function toAsciiHex(string $string): string 
{
    return join(array_map(function ($byte) { return "%$byte"; }, str_split(bin2hex($string), 2)));
}