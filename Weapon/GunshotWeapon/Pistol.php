<?php


namespace Weapon;


class Pistol extends GunshotWeapon
{
    private $armorPiercing;

    final public function getArmorPiercing(){
        return $this->armorPiercing;
    }
    final public function setArmorPiercing(float $armorPiercing){
        $this->armorPiercing = $armorPiercing;
    }
}