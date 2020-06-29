<?php

namespace Weapon;

abstract class Weapon
{
    private $name;
    private $price;

    final public function __construct(float $price,string $name)
    {
        $this->name =$name;
        $this->price = $price;
    }

    final public function getPrice(){
        return $this->price;
    }
    final public function getName(){
        return $this->name;
    }

}