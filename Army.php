<?php

namespace Army;

class Army
{
    private $soldiers = [];
    private $weaponPrice;
    final public function __construct(Soldier ...$soldier){
        $this->soldiers[] = $soldier;
    }

    final public function getArmyWeaponPrice(){

        foreach ($this->soldiers as $key ){
            foreach($key as $soldier){
                $this->weaponPrice += $soldier->getWeaponPrice();
            }
        }
        return $this->weaponPrice;
    }
}
