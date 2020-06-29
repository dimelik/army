<?php
namespace Weapon;



abstract class GunshotWeapon extends Weapon{
    private $caliber;
    private $range;

    final public function setRange(int $range)
    {
        $this->range = $range;
    }

    final public function setCaliber(float $caliber){
        $this->caliber = $caliber;
    }
    final public function getCaliber(){
        return $this->caliber;
    }
    final public function getRange(){
        return $this->range;
    }
}