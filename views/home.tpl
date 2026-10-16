<html>
	<head>
		<title>
			BTC App by Kamal Sir
		</title>
		<style>
			*{
				font-size:40px;
				text-align:center;
			}
			body{
				background-color:honeydew;
			}
		</style>
	</head>
	<body>
		<h1>BTC APP</h1>
		<form method="POST">
			<input type="number"
					name="num"
					placeholder="Enter Number of Bitcoins"
					required
					min=1
			/>
			<br/><br/>
			<input type="submit"
					value="Find Amount"
			/>
		</form>
		<h2>
			{{msg}}
		</h2>
	</body>
</html>