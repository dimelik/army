<?php
namespace Army;
require_once "Weapon/Weapon.php";
require_once "Weapon/ColdWeapon/ColdWeapon.php";
require_once "Weapon/GunshotWeapon/GunshotWeapon.php";
require_once "Weapon/GunshotWeapon/Automatic.php";
require_once "Weapon/GunshotWeapon/Pistol.php";
require_once "Weapon/ColdWeapon/Knife.php";
require_once "Weapon/ColdWeapon/SapperBlade.php";
require_once "Soldier.php";
require_once "Army.php";

use Weapon\Knife;
use Weapon\SapperBlade;
use Weapon\Automatic;
use Weapon\Pistol;


$pistol = new Pistol("3000", "colt");

$knife = new Knife('200', 'Knife');

$automatic = new Automatic('5000', 'AK');

$sapperBlade = new sapperBlade('200', 'Sapper');

$soldier = new Soldier();
$soldier->setAutomatic($automatic);
$soldier->setKnife($knife);
$soldier->setPistol($pistol);
$soldier->setSapperBlade($sapperBlade);


$army = new Army($soldier, $soldier, $soldier, $soldier);
$priceWeapon = $army->getArmyWeaponPrice();
echo "$priceWeapon <br>";

$knife->setArmorPiercing("12.2");
$knifePiercing = $knife->getArmorPiercing();
echo "$knifePiercing";