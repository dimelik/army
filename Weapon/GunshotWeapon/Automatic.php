<?php


namespace Weapon;


class Automatic extends GunshotWeapon
{
    private $rateFire;

    final public function getRateFire(){
        return $this->rateFire;
    }
    final public function setRateFire(float $rateFire){
        $this->rateFire = $rateFire;
    }

}