<?php

namespace Army;

use Weapon\Weapon;

class Soldier
{
    private $knife;
    private $sapperBlade;
    private $automatic;
    private $pistol;
    private $weaponPrice;

    final public function setKnife(Weapon $knife)
    {
        $this->knife = $knife;
        $this->weaponPrice += $knife->getPrice();
    }

    final public function setPistol(Weapon $sapperBlade)
    {
        $this->sapperBlade = $sapperBlade;
        $this->weaponPrice += $sapperBlade->getPrice();
    }

    final public function setAutomatic(Weapon $automatic)
    {
        $this->automatic = $automatic;
        $this->weaponPrice += $automatic->getPrice();
    }

    final public function setSapperBlade(Weapon $pistol)
    {
        $this->pistol = $pistol;
        $this->weaponPrice += $pistol->getPrice();
    }

    final public function getWeaponPrice()
    {
        return $this->weaponPrice;
    }

    final public function getAutomatic()
    {
        return $this->automatic;
    }

    final public function getPistol()
    {
        return $this->pistol;
    }

    final public function getKnife()
    {
        return $this->knife;
    }

    final public function getSapperBlade()
    {
        return $this->sapperBlade;
    }
}