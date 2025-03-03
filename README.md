<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ягуар</title>
    <style>
        /* Общие стили */
        body {
            font-family: Arial, sans-serif;
            background-color: #eef;
            color: #333;
            text-align: justify;
            margin: 0;
            padding: 0;
        }
        
        /* Шапка */
        .header {
            background-color: #0077cc;
            color: white;
            padding: 10px;
            text-align: center;
            font-size: 18pt;
        }
        
        /* Меню */
        .menu {
            width: 20%;
            float: left;
            background-color: #ccc;
            padding: 10px;
            height: 100vh;
        }
        
        .menu ul {
            list-style-type: none;
            padding: 0;
        }
        
        .menu li {
            margin: 10px 0;
        }
        
        .menu a {
            text-decoration: none;
            color: #0077cc;
            font-size: 18pt;
        }
        
        .menu a:hover {
            color: #ff6600;
        }
        
        /* Контент */
        .content {
            width: 75%;
            float: right;
            padding: 20px;
        }
        
        h1 {
            font-size: 24pt;
            color: #0055aa;
        }
        
        p {
            font-size: 18pt;
        }
        
        /* Очистка потока */
        .clearfix {
            content: "";
            display: table;
            clear: both;
        }
        
        /* Бегущая строка */
        .marquee {
            font-size: 18pt;
            background-color: #0077cc;
            color: white;
            padding: 5px;
            white-space: nowrap;
            overflow: hidden;
            display: block;
        }
    </style>
</head>
<body>

    <!-- Бегущая строка -->
    <div class="header">
        <marquee>Ягуар — хищник из семейства кошачьих, обитающий в Южной Америке</marquee>
    </div>

    <div class="clearfix">
        <!-- Меню -->
        <div class="menu">
            <ul>
                <li><a href="#" onclick="showPage('home')">Главная</a></li>
                <li><a href="#" onclick="showPage('info')">Основная информация</a></li>
                <li><a href="#" onclick="showPage('extra')">Дополнительно</a></li>
            </ul>
        </div>

        <!-- Контент -->
        <div class="content" id="content">
            <div id="home">
                <h1>Ягуар</h1>
                <p>Ягуар — один из самых крупных хищников Южной Америки, обладающий мощным укусом.</p>
                <img src="jaguar.jpg" alt="Ягуар" width="100%">
            </div>

            <div id="info" style="display: none;">
                <h1>Основная информация о ягуаре</h1>
                <p>Ягуар (Panthera onca) — единственный представитель рода пантер в Америке. Он занимает третье место по величине среди кошачьих после тигра и льва. Ягуары ведут одиночный образ жизни и предпочитают лесистую местность.</p>
                <p>Средний вес самца составляет 80-120 кг, самки — 60-90 кг.</p>
            </div>

            <div id="extra" style="display: none;">
                <h1>Дополнительная информация</h1>
                <p>Ягуары охотятся на самых разных животных: от рыбы до крупных копытных. Они обладают мощной челюстью, способной пробивать череп добычи.</p>
                <p>Популяция ягуаров сокращается из-за уничтожения их естественной среды обитания.</p>
            </div>
        </div>
    </div>

    <script>
        function showPage(page) {
            document.getElementById("home").style.display = "none";
            document.getElementById("info").style.display = "none";
            document.getElementById("extra").style.display = "none";

            document.getElementById(page).style.display = "block";
        }
    </script>

</body>
</html>
