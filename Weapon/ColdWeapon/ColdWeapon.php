<?php

namespace Weapon;


abstract class ColdWeapon extends Weapon {
    protected $bladeLength;
    protected $material;

    final public function getMaterial(){
        return $this->material;
    }

    final public function getBladeLength(){
        return $this->bladeLength;
    }
    final public function setBladeLength(float $bladeLength){
        $this->bladeLength = $bladeLength;
    }
    final public function setMaterial(string $material){
        $this->material = $material;
    }

}