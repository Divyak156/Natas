<?php
	$orig = base64_decode('ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw');

	function xor_encrypt($in) {
		$key = json_encode(array("showpassword"=>"no", "bgcolor"=>"#ffffff"));
		$text = $in;
		$outText = '';

		for($i=0;$i<strlen($text);$i++) {
			$outText .= $text[$i] ^ $key[$i % strlen($key)];
		}

		return $outText;
	}

	print xor_encrypt($orig);

?>
