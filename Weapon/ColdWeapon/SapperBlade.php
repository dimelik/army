<?php


namespace Weapon;


class SapperBlade extends ColdWeapon
{
    private $handleLength;

    final public function getHandleLength(){
        return $this->handleLength;
    }

    final public function setHandleLength(float $handleLength){
        $this->handleLength = $handleLength;
    }
}