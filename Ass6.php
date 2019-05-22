
BlackJack: 


<?php
$deck = array();
$suits = array("of_spades", "of_clubs", "of_diamonds", "of_hearts");
$numbers = array('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13');
foreach($suits as $suit) {
    foreach($numbers as $number){
        $deck[] = array($number, $suit);
    }
}
$playerdeck = array();
$dealerdeck = array();

while (sizeof($playerdeck) < 3){
    $p = mt_rand(1,52);
    $pcard = $deck[$p];
    if (in_array($pcard, $playerdeck)){
    }
    else{
        array_push($playerdeck,$pcard );
    }
}

while (sizeof($dealerdeck) < 3){
    $d = mt_rand(1,52);
    $dcard = $deck[$d];
    if (in_array($dcard, $playerdeck)){
    }
    
    elseif(in_array($dcard, $playerdeck)){
    }
    else{
        array_push($dealerdeck,$dcard );
    }
}

print_r($playerdeck);
print_r($dealerdeck);
 
$dealerfirst_card = $dealerdeck[0];
$dealersecond_card = $dealerdeck[1];
$dealerthird_card  = $dealerdeck[2];

$playerfirst_card = $playerdeck[0];
$playersecond_card = $playerdeck[1];
$playerthird_card = $playerdeck[2];

$dealers = $dealerfirst_card[0] + $dealersecond_card[0] + $dealerthird_card[0];

$players = $playerfirst_card[0] + $playersecond_card[0] ;

echo "You have these cards:"; 
print_r($playerfirst_card);
print_r($playersecond_card);
echo "Your cards make a combined total of:" . " " .$players;

?>

<form action=""  method="POST">
    <input type="text" name="userinput" placeholder="Hit or Stay"><br>
    <input type="submit" name="check" value="Check">
</form>

<?php
$userinput= $_POST['userinput'];
$checkbutton= $_POST['check'];

if ($checkbutton){
    if($userinput == "hit"){
        $current = $playerfirst_card[0] + $playersecond_card[0] +  $playerthird_card[0] ;
        echo "You now have:"." " . $current . " "; 
        echo "With these cards:";
        print_r($playerfirst_card);
        print_r($playersecond_card);
        print_r($playerthird_card);
        echo "Dealer now has:" . " " . $dealers;
        echo "With these cards:"; 
        print_r($dealerfirst_card);
        print_r($dealersecond_card);
        print_r($dealerthird_card);
        
        if ($current <= 21 && $dealers <= 21){
            if($dealers == $current){
                echo "It's a tie!";
            }
            
            if ($current < $dealers){
                echo "Dealer Wins :(";
            }
            if ($current > $dealers){
                echo "You Win!";
            }
        }
        else{
            if ($current > 21){
                echo "You Busted! Dealer Wins :(";
            }
            if ($dealers> 21){
                echo "Dealer Busted! You Win!";
            }
        }

    }

    else{
        echo "Dealer now has:" . " " . $dealers;
        echo "With these cards:";
        print_r($dealerfirst_card);
        print_r($dealersecond_card);
        print_r($dealerthird_card);
        if ($players <= 21 && $dealers <= 21){
            if($dealers == $players){
                echo "It's a tie!";
            }
            
            if ($players < $dealers){
                echo "Dealer Wins :(";
            }
            if ($players > $dealers){
                echo "You Win!";
            }
        }
        else{
            if ($players > 21){
                echo "You Busted! Dealer Wins :(";
            }
            if ($dealers> 21){
                echo "Dealer Busted! You Win!";
            }
        }
    }
}

?>