<?php

	function xor_encrypt() {
		$key = "qw8J";
		$text = json_encode(array("showpassword"=>"yes", "bgcolor"=>"#ffffff"));
		$outText = '';

		for($i=0;$i<strlen($text);$i++) {
			$outText .= $text[$i] ^ $key[$i % strlen($key)];
		}

		return $outText;
	}

	print base64_encode(xor_encrypt());

?>
