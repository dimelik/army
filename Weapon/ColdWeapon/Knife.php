<?php


namespace Weapon;


class Knife extends ColdWeapon
{
    private $armorPiercing;

    final public function getArmorPiercing(){
        return $this->armorPiercing;
    }
    final public function setArmorPiercing(float $armorPiercing){
        $this->armorPiercing = $armorPiercing;
    }

}