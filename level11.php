#!/usr/bin/php7.0
<?php
$defaultdata = array( "showpassword"=>"no", "bgcolor"=>"#ffffff");

function xor_encrypt($in, $key) {
    
    $text = $in;
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
    $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}

$plaintext = json_encode($defaultdata);
$ciphertext=hex2bin('0a554b221e00482b02044f2503131a70531957685d555a2d121854250355026852115e2c17115e680c');
//echo($plaintext);
//echo($ciphertext);
//echo(xor_encrypt($plaintext, $ciphertext));
$key= 'qw8J';
$gooddata = json_encode(array( "showpassword"=>"yes", "bgcolor"=>"#ffffff"));
echo(base64_encode(xor_encrypt($gooddata, $key)));



//$xor1=0^0;
//$xor2=0^1;
//$xor3=1^0;
//$xor4=1^1;
//echo("\n1 XOR 0^0 wynosi: ".$xor1);
//echo("\n2 XOR 0^1 wynosi: ".$xor2);
//echo("\n3 XOR 1^0 wynosi: ".$xor3);
//echo("\n4 XOR 1^1 wynosi: ".$xor4);
//echo("\n");
?>
