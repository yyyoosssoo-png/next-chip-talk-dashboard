<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Next Chip Talk 교육 성과 분석</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/3.9.1/chart.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/wordcloud2.js/1.2.2/wordcloud2.min.js"></script>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;700;900&family=Noto+Sans+KR:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Noto Sans KR', '맑은고딕', sans-serif;
            background: linear-gradient(135deg, #000000 0%, #0a0a1a 30%, #1a1a2e 70%, #0a0a1a 100%);
            background-size: 400% 400%;
            animation: gradientShift 20s ease infinite;
            min-height: 100vh;
            color: #ffffff;
            position: relative;
            overflow-x: hidden;
        }
        
        @keyframes gradientShift {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        
        body::before {
            content: '';
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: 
                radial-gradient(2px 2px at 20px 30px, rgba(255, 255, 255, 0.8), transparent),
                radial-gradient(2px 2px at 40px 70px, rgba(168, 85, 247, 0.6), transparent),
                radial-gradient(1px 1px at 90px 40px, rgba(255, 255, 255, 0.4), transparent),
                radial-gradient(1px 1px at 130px 80px, rgba(236, 72, 153, 0.5), transparent),
                radial-gradient(2px 2px at 160px 30px, rgba(255, 255, 255, 0.3), transparent),
                radial-gradient(1px 1px at 200px 90px, rgba(6, 182, 212, 0.4), transparent),
                radial-gradient(1px 1px at 250px 50px, rgba(255, 255, 255, 0.6), transparent),
                radial-gradient(2px 2px at 300px 20px, rgba(168, 85, 247, 0.3), transparent),
                radial-gradient(1px 1px at 350px 60px, rgba(255, 255, 255, 0.5), transparent);
            background-repeat: repeat;
            background-size: 350px 200px;
            animation: sparkle 25s linear infinite;
            pointer-events: none;
            z-index: -1;
        }
        
        @keyframes sparkle {
            0% { transform: translate(0, 0); }
            100% { transform: translate(-350px, -200px); }
        }
        
        .container {
            max-width: 1400px;
            margin: 0 auto;
            padding: 20px;
            position: relative;
            z-index: 1;
        }
        
        .header {
            text-align: center;
            margin-bottom: 40px;
            position: relative;
        }
        
        .logo-area {
            margin-bottom: 30px;
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        
        .nct-logo-img {
            max-width: 350px;
            width: 100%;
            height: auto;
            margin-bottom: 25px;
            filter: drop-shadow(0 10px 30px rgba(168, 85, 247, 0.3));
            transition: all 0.3s ease;
        }
        
        .nct-logo-img:hover {
            transform: translateY(-5px);
            filter: drop-shadow(0 20px 40px rgba(168, 85, 247, 0.4));
        }
        
        .header h1 {
            font-family: 'Orbitron', monospace;
            font-size: 2.4rem;
            margin: 25px 0 15px 0;
            color: #ffffff;
            font-weight: 600;
            letter-spacing: 0.05em;
            text-shadow: 0 5px 15px rgba(255, 255, 255, 0.1);
        }
        
        .header p {
            font-size: 1.1rem;
            color: #b8b9ff;
            font-weight: 300;
            line-height: 1.6;
        }
        
        .accent-line {
            width: 120px;
            height: 4px;
            background: linear-gradient(90deg, #a855f7, #ec4899, #06b6d4);
            margin: 25px auto;
            border-radius: 2px;
            box-shadow: 0 0 20px rgba(168, 85, 247, 0.5);
        }
        
        .nav-tabs {
            display: flex;
            background: rgba(255, 255, 255, 0.08);
            border-radius: 16px;
            margin-bottom: 40px;
            padding: 8px;
            backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.12);
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        }
        
        .nav-tab {
            flex: 1;
            padding: 16px 20px;
            text-align: center;
            background: transparent;
            color: #d1d5db;
            border: none;
            border-radius: 12px;
            cursor: pointer;
            transition: all 0.4s ease;
            font-weight: 500;
            font-family: 'Noto Sans KR', sans-serif;
            position: relative;
            overflow: hidden;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
        }
        
        .nav-tab::before {
            content: '';
            width: 16px;
            height: 16px;
            border-radius: 3px;
            transition: all 0.3s ease;
        }
        
        .nav-tab[data-tab="overview"]::before {
            background: linear-gradient(135deg, #a855f7, #ec4899);
            clip-path: polygon(0% 20%, 20% 0%, 100% 0%, 100% 80%, 80% 100%, 0% 100%);
        }
        
        .nav-tab[data-tab="composition"]::before {
            background: linear-gradient(135deg, #06b6d4, #10b981);
            clip-path: polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%);
        }
        
        .nav-tab[data-tab="feedback"]::before {
            background: linear-gradient(135deg, #ec4899, #f59e0b);
            border-radius: 50%;
            position: relative;
        }
        
        .nav-tab[data-tab="insights"]::before {
            background: linear-gradient(135deg, #f59e0b, #a855f7);
            clip-path: polygon(50% 0%, 0% 100%, 100% 100%);
        }
        
        .nav-tab::after {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.1), transparent);
            transition: left 0.6s ease;
        }
        
        .nav-tab:hover::after {
            left: 100%;
        }
        
        .nav-tab.active {
            background: linear-gradient(135deg, #a855f7, #ec4899);
            color: white;
            transform: translateY(-3px);
            box-shadow: 0 12px 30px rgba(168, 85, 247, 0.4);
        }
        
        .nav-tab:hover:not(.active) {
            background: rgba(255, 255, 255, 0.15);
            transform: translateY(-2px);
            box-shadow: 0 8px 25px rgba(255, 255, 255, 0.1);
        }
        
        .tab-content {
            display: none;
            animation: fadeInUp 0.6s ease;
        }
        
        .tab-content.active {
            display: block;
        }
        
        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        .kpi-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 25px;
            margin-bottom: 40px;
        }
        
        .kpi-card {
            background: rgba(255, 255, 255, 0.08);
            padding: 30px 25px;
            border-radius: 20px;
            text-align: center;
            backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.12);
            transition: all 0.4s ease;
            position: relative;
            overflow: hidden;
        }
        
        .kpi-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 2px;
            background: linear-gradient(90deg, #a855f7, #ec4899, #06b6d4);
            transform: translateX(-100%);
            transition: transform 0.6s ease;
        }
        
        .kpi-card:hover::before {
            transform: translateX(0);
        }
        
        .kpi-card:hover {
            transform: translateY(-8px);
            box-shadow: 0 20px 50px rgba(168, 85, 247, 0.25);
            background: rgba(255, 255, 255, 0.12);
        }
        
        .kpi-value {
            font-size: 3rem;
            font-weight: 700;
            background: linear-gradient(135deg, #a855f7, #ec4899, #06b6d4);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 12px;
            text-shadow: 0 0 30px rgba(168, 85, 247, 0.5);
        }
        
        .kpi-label {
            font-size: 1.1rem;
            color: #e5e7eb;
            margin-bottom: 8px;
            font-weight: 500;
        }
        
        .kpi-desc {
            font-size: 0.95rem;
            color: #9ca3af;
            opacity: 0.8;
        }
        
        .chart-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(450px, 1fr));
            gap: 30px;
            margin-bottom: 40px;
        }
        
        .chart-container {
            background: rgba(255, 255, 255, 0.08);
            padding: 30px;
            border-radius: 20px;
            backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.12);
            transition: all 0.3s ease;
            position: relative;
        }
        
        .chart-container:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 40px rgba(0, 0, 0, 0.2);
        }
        
        .chart-title {
            font-size: 1.3rem;
            font-weight: 600;
            margin-bottom: 25px;
            color: #ffffff;
            text-align: center;
            position: relative;
        }
        
        .chart-title::after {
            content: '';
            position: absolute;
            bottom: -8px;
            left: 50%;
            transform: translateX(-50%);
            width: 50px;
            height: 2px;
            background: linear-gradient(90deg, #a855f7, #ec4899);
            border-radius: 1px;
        }
        
        .wordcloud-container {
            background: rgba(255, 255, 255, 0.08);
            padding: 30px;
            border-radius: 20px;
            backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.12);
            margin-bottom: 40px;
            min-height: 450px;
        }
        
        .session-filter {
            display: flex;
            justify-content: center;
            gap: 12px;
            margin-bottom: 25px;
            flex-wrap: wrap;
        }
        
        .filter-btn {
            padding: 10px 20px;
            border: 2px solid rgba(168, 85, 247, 0.6);
            background: rgba(168, 85, 247, 0.1);
            color: #a855f7;
            border-radius: 30px;
            cursor: pointer;
            transition: all 0.3s ease;
            font-size: 0.9rem;
            font-family: 'Noto Sans KR', sans-serif;
            font-weight: 500;
            backdrop-filter: blur(10px);
        }
        
        .filter-btn.active {
            background: linear-gradient(135deg, #a855f7, #ec4899);
            color: white;
            border-color: transparent;
            box-shadow: 0 5px 20px rgba(168, 85, 247, 0.4);
        }
        
        .filter-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 25px rgba(168, 85, 247, 0.3);
        }
        
        .sentiment-dashboard {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
            gap: 25px;
            margin-bottom: 40px;
        }
        
        .sentiment-card {
            background: rgba(255, 255, 255, 0.08);
            padding: 25px;
            border-radius: 20px;
            backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.12);
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        }
        
        .sentiment-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 4px;
            height: 100%;
            transition: width 0.3s ease;
        }
        
        .sentiment-card.positive::before {
            background: linear-gradient(180deg, #10b981, #059669);
        }
        
        .sentiment-card.negative::before {
            background: linear-gradient(180deg, #ef4444, #dc2626);
        }
        
        .sentiment-card.neutral::before {
            background: linear-gradient(180deg, #f59e0b, #d97706);
        }
        
        .sentiment-card:hover::before {
            width: 8px;
        }
        
        .sentiment-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 40px rgba(0, 0, 0, 0.2);
        }
        
        .sentiment-header {
            display: flex;
            align-items: center;
            margin-bottom: 18px;
        }
        
        .sentiment-icon {
            font-size: 1.6rem;
            margin-right: 12px;
        }
        
        .sentiment-title {
            font-size: 1.2rem;
            font-weight: 600;
            color: #ffffff;
        }
        
        .sentiment-count {
            font-size: 2.4rem;
            font-weight: 700;
            margin-bottom: 12px;
        }
        
        .sentiment-examples {
            font-size: 0.95rem;
            color: #d1d5db;
            line-height: 1.5;
            opacity: 0.9;
        }
        
        .composition-evolution {
            background: rgba(255, 255, 255, 0.08);
            padding: 30px;
            border-radius: 20px;
            backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.12);
            margin-bottom: 40px;
        }
        
        .evolution-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 25px;
            margin-top: 30px;
        }
        
        .session-composition {
            text-align: center;
            padding: 20px;
            border-radius: 16px;
            background: rgba(255, 255, 255, 0.06);
            border: 1px solid rgba(255, 255, 255, 0.08);
            transition: all 0.3s ease;
        }
        
        .session-composition:hover {
            background: rgba(255, 255, 255, 0.1);
            transform: translateY(-3px);
        }
        
        .session-title {
            font-weight: 600;
            margin-bottom: 8px;
            color: #a855f7;
            font-size: 0.95rem;
            line-height: 1.3;
        }
        
        .session-topic {
            font-size: 0.8rem;
            color: #9ca3af;
            margin-bottom: 15px;
            font-style: italic;
            opacity: 0.8;
        }
        
        .dept-bar {
            margin: 10px 0;
            display: flex;
            align-items: center;
        }
        
        .dept-name {
            width: 70px;
            font-size: 0.8rem;
            text-align: left;
            color: #e5e7eb;
        }
        
        .dept-progress {
            flex: 1;
            height: 8px;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 10px;
            margin: 0 8px;
            overflow: hidden;
        }
        
        .dept-fill {
            height: 100%;
            border-radius: 10px;
            transition: width 0.8s ease;
            box-shadow: 0 0 10px rgba(168, 85, 247, 0.3);
        }
        
        .dept-percent {
            font-size: 0.8rem;
            min-width: 35px;
            color: #d1d5db;
            font-weight: 500;
        }
        
        .insight-section {
            background: rgba(255, 255, 255, 0.08);
            padding: 35px;
            border-radius: 20px;
            margin-bottom: 40px;
            backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.12);
        }
        
        .insight-title {
            font-size: 1.6rem;
            font-weight: 600;
            margin-bottom: 25px;
            color: #ffffff;
            display: flex;
            align-items: center;
        }
        
        .insight-title::before {
            content: '';
            width: 24px;
            height: 24px;
            margin-right: 12px;
            background: linear-gradient(135deg, #f59e0b, #a855f7);
            clip-path: polygon(50% 0%, 0% 100%, 100% 100%);
            filter: drop-shadow(0 0 8px rgba(245, 158, 11, 0.4));
        }
        
        .education-overview {
            background: linear-gradient(135deg, rgba(168, 85, 247, 0.2), rgba(236, 72, 153, 0.2));
            padding: 35px;
            border-radius: 20px;
            margin-bottom: 40px;
            border: 1px solid rgba(255, 255, 255, 0.15);
            backdrop-filter: blur(20px);
        }
        
        .education-title {
            font-size: 2rem;
            font-weight: 600;
            margin-bottom: 30px;
            text-align: center;
            color: #ffffff;
        }
        
        .education-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 25px;
        }
        
        .education-item {
            background: rgba(255, 255, 255, 0.12);
            padding: 25px;
            border-radius: 16px;
            backdrop-filter: blur(15px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            transition: all 0.3s ease;
        }
        
        .education-item:hover {
            transform: translateY(-3px);
            background: rgba(255, 255, 255, 0.18);
        }
        
        .education-item h4 {
            font-size: 1.2rem;
            font-weight: 600;
            margin-bottom: 12px;
            color: #ffffff;
        }
        
        .education-item p, .education-item ul {
            font-size: 0.95rem;
            line-height: 1.6;
            color: rgba(255, 255, 255, 0.9);
        }
        
        .education-item ul {
            padding-left: 0;
            list-style: none;
        }
        
        .education-item li {
            margin-bottom: 10px;
            padding-left: 20px;
            position: relative;
        }
        
        .education-item li::before {
            content: "▸";
            position: absolute;
            left: 0;
            color: #fbbf24;
            font-weight: bold;
        }
        
        .insight-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
            gap: 25px;
        }
        
        .insight-card {
            padding: 25px;
            border-left: 4px solid #a855f7;
            background: rgba(255, 255, 255, 0.06);
            border-radius: 12px;
            border: 1px solid rgba(255, 255, 255, 0.08);
            transition: all 0.3s ease;
            position: relative;
        }
        
        .insight-card:hover {
            background: rgba(255, 255, 255, 0.1);
            transform: translateY(-3px);
            box-shadow: 0 10px 30px rgba(168, 85, 247, 0.15);
        }
        
        .insight-card h4 {
            color: #a855f7;
            margin-bottom: 15px;
            font-weight: 600;
            font-size: 1.1rem;
            display: flex;
            align-items: center;
            gap: 10px;
        }
        
        .insight-card h4::before {
            content: '';
            width: 16px;
            height: 16px;
            border-radius: 2px;
        }
        
        .insight-card h4[data-icon="target"]::before {
            background: linear-gradient(135deg, #a855f7, #ec4899);
            clip-path: circle(50%);
            position: relative;
        }
        
        .insight-card h4[data-icon="chart"]::before {
            background: linear-gradient(135deg, #06b6d4, #10b981);
            clip-path: polygon(0% 100%, 0% 60%, 25% 40%, 50% 70%, 75% 20%, 100% 50%, 100% 100%);
        }
        
        .insight-card h4[data-icon="cycle"]::before {
            background: linear-gradient(135deg, #10b981, #f59e0b);
            border-radius: 50%;
            border: 2px solid #10b981;
            background-clip: padding-box;
        }
        
        .insight-card h4[data-icon="growth"]::before {
            background: linear-gradient(135deg, #ec4899, #a855f7);
            clip-path: polygon(0% 100%, 20% 60%, 40% 80%, 60% 40%, 80% 60%, 100% 0%, 100% 100%);
        }
        
        .insight-card h4[data-icon="lightbulb"]::before {
            background: linear-gradient(135deg, #f59e0b, #a855f7);
            clip-path: circle(40%);
            filter: drop-shadow(0 0 6px rgba(245, 158, 11, 0.6));
        }
        
        .insight-card h4[data-icon="gear"]::before {
            background: linear-gradient(135deg, #06b6d4, #ec4899);
            clip-path: polygon(50% 0%, 80% 10%, 100% 35%, 90% 70%, 65% 100%, 35% 100%, 10% 70%, 0% 35%, 20% 10%);
        }
        
        .insight-card h4[data-icon="money"]::before {
            background: linear-gradient(135deg, #f59e0b, #ec4899);
            clip-path: polygon(30% 0%, 70% 0%, 100% 30%, 100% 70%, 70% 100%, 30% 100%, 0% 70%, 0% 30%);
        }
        
        .insight-card h4[data-icon="loop"]::before {
            background: linear-gradient(135deg, #10b981, #06b6d4);
            border-radius: 50%;
            border: 3px solid transparent;
            background-clip: padding-box;
            position: relative;
        }
        
        .insight-card ul {
            padding-left: 20px;
        }
        
        .insight-card li {
            margin-bottom: 10px;
            color: #e5e7eb;
            line-height: 1.5;
        }
        
        .request-detail {
            display: none;
            margin-top: 18px;
            padding: 18px;
            background: rgba(255, 255, 255, 0.06);
            border-radius: 10px;
            border-left: 3px solid #a855f7;
            transition: all 0.3s ease;
        }
        
        .request-detail.active {
            display: block;
            animation: slideDown 0.3s ease;
        }
        
        @keyframes slideDown {
            from {
                opacity: 0;
                transform: translateY(-10px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        .request-detail h5 {
            color: #a855f7;
            margin-bottom: 12px;
            font-weight: 600;
        }
        
        .request-detail ul {
            padding-left: 20px;
        }
        
        .request-detail li {
            margin-bottom: 8px;
            color: #d1d5db;
            font-size: 0.9rem;
            line-height: 1.4;
        }
        
        .clickable {
            cursor: pointer;
            transition: all 0.2s ease;
        }
        
        .clickable:hover {
            color: #ec4899;
        }
        
        @media (max-width: 768px) {
            .header h1 {
                font-size: 1.8rem;
            }
            
            .nct-logo-img {
                max-width: 280px;
            }
            
            .chart-grid {
                grid-template-columns: 1fr;
            }
            
            .nav-tabs {
                flex-direction: column;
            }
            
            .evolution-grid {
                grid-template-columns: repeat(2, 1fr);
            }
            
            .education-grid {
                grid-template-columns: 1fr;
            }
            
            .kpi-grid {
                grid-template-columns: repeat(2, 1fr);
            }
            
            .kpi-value {
                font-size: 2.2rem;
            }
        }
        
        @media (max-width: 480px) {
            .evolution-grid {
                grid-template-columns: 1fr;
            }
            
            .kpi-grid {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <div class="logo-area">
                <img src="nct-logo.png" alt="Next Chip Talk Logo" class="nct-logo-img" 
                     onerror="this.style.display='none'; document.getElementById('fallback-logo').style.display='block';">
                <div id="fallback-logo" style="display: none; font-family: 'Orbitron', monospace; font-size: 4rem; font-weight: 300; color: #ffffff; letter-spacing: 0.2em; margin-bottom: 20px;">nct</div>
            </div>
            <h1>Next Chip Talk 교육 성과 분석</h1>
            <p>2025 미래반도체 Next & Grey 영역 교육 성과</p>
            <div class="accent-line"></div>
        </div>

        <div class="nav-tabs">
            <button class="nav-tab active" data-tab="overview" onclick="showTab('overview')">종합 개요</button>
            <button class="nav-tab" data-tab="composition" onclick="showTab('composition')">참가자 구성 변화</button>
            <button class="nav-tab" data-tab="feedback" onclick="showTab('feedback')">피드백 분석</button>
            <button class="nav-tab" data-tab="insights" onclick="showTab('insights')">전략적 인사이트</button>
        </div>

        <!-- 종합 개요 탭 -->
        <div id="overview" class="tab-content active">
            <div class="kpi-grid">
                <div class="kpi-card">
                    <div class="kpi-value">118명</div>
                    <div class="kpi-label">총 참가자</div>
                    <div class="kpi-desc">4회차 누적</div>
                </div>
                <div class="kpi-card">
                    <div class="kpi-value">4.50</div>
                    <div class="kpi-label">평균 만족도</div>
                    <div class="kpi-desc">5점 만점</div>
                </div>
                <div class="kpi-card">
                    <div class="kpi-value">95.1%</div>
                    <div class="kpi-label">평균 추천률</div>
                    <div class="kpi-desc">매우 높은 수준</div>
                </div>
                <div class="kpi-card">
                    <div class="kpi-value">380%</div>
                    <div class="kpi-label">추정 ROI</div>
                    <div class="kpi-desc">투자 대비 효과</div>
                </div>
            </div>

            <div class="chart-grid">
                <div class="chart-container">
                    <div class="chart-title">회차별 만족도 추이</div>
                    <canvas id="satisfactionChart"></canvas>
                </div>
                <div class="chart-container">
                    <div class="chart-title">회차별 추천률 변화</div>
                    <canvas id="recommendationChart"></canvas>
                </div>
            </div>

            <div class="insight-section">
                <div class="insight-title">주요 성과 요약</div>
                <div class="insight-grid">
                    <div class="insight-card">
                        <h4 data-icon="target">교육 효과성</h4>
                        <ul>
                            <li>만족도 4.5/5점으로 목표 대비 125% 달성</li>
                            <li>추천률 95.1%로 업계 최고 수준</li>
                            <li>4회차 연속 안정적 품질 유지</li>
                        </ul>
                    </div>
                    <div class="insight-card">
                        <h4 data-icon="chart">참가자 특성</h4>
                        <ul>
                            <li>SK하이닉스 임직원 중심 구성 (76%)</li>
                            <li>시니어(10년+) 71.2% 참여로 질적 수준 확보</li>
                            <li>R&D→사업전략→제조기술 순 참여</li>
                        </ul>
                    </div>
                    <div class="insight-card">
                        <h4 data-icon="cycle">기술 트렌드 제공</h4>
                        <ul>
                            <li>광통신 → 유리기판 → AI메모리 → NAND</li>
                            <li>신기술에서 응용기술로 진화</li>
                            <li>시장분석과 기술설명 균형 유지</li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>

        <!-- 참가자 구성 변화 탭 -->
        <div id="composition" class="tab-content">
            <div class="composition-evolution">
                <div class="chart-title">회차별 참가자 구성 변화</div>
                <div class="evolution-grid">
                    <div class="session-composition">
                        <div class="session-title">1회차 (4.18)</div>
                        <div class="session-topic">Optical Interconnection</div>
                        <div class="dept-bar">
                            <div class="dept-name">R&D</div>
                            <div class="dept-progress">
                                <div class="dept-fill" style="width: 45%; background: linear-gradient(90deg, #a855f7, #ec4899);"></div>
                            </div>
                            <div class="dept-percent">45%</div>
                        </div>
                        <div class="dept-bar">
                            <div class="dept-name">사업전략</div>
                            <div class="dept-progress">
                                <div class="dept-fill" style="width: 35%; background: linear-gradient(90deg, #06b6d4, #0ea5e9);"></div>
                            </div>
                            <div class="dept-percent">35%</div>
                        </div>
                        <div class="dept-bar">
                            <div class="dept-name">제조/기술</div>
                            <div class="dept-progress">
                                <div class="dept-fill" style="width: 20%; background: linear-gradient(90deg, #10b981, #059669);"></div>
                            </div>
                            <div class="dept-percent">20%</div>
                        </div>
                    </div>

                    <div class="session-composition">
                        <div class="session-title">2회차 (6.25)</div>
                        <div class="session-topic">Glass Substrate</div>
                        <div class="dept-bar">
                            <div class="dept-name">사업전략</div>
                            <div class="dept-progress">
                                <div class="dept-fill" style="width: 50%; background: linear-gradient(90deg, #06b6d4, #0ea5e9);"></div>
                            </div>
                            <div class="dept-percent">50%</div>
                        </div>
                        <div class="dept-bar">
                            <div class="dept-name">R&D</div>
                            <div class="dept-progress">
                                <div class="dept-fill" style="width: 25%; background: linear-gradient(90deg, #a855f7, #ec4899);"></div>
                            </div>
                            <div class="dept-percent">25%</div>
                        </div>
                        <div class="dept-bar">
                            <div class="dept-name">제조/기술</div>
                            <div class="dept-progress">
                                <div class="dept-fill" style="width: 25%; background: linear-gradient(90deg, #10b981, #059669);"></div>
                            </div>
                            <div class="dept-percent">25%</div>
                        </div>
                    </div>

                    <div class="session-composition">
                        <div class="session-title">3회차 (7.30)</div>
                        <div class="session-topic">AI Chip 메모리 시스템</div>
                        <div class="dept-bar">
                            <div class="dept-name">사업전략</div>
                            <div class="dept-progress">
                                <div class="dept-fill" style="width: 52%; background: linear-gradient(90deg, #06b6d4, #0ea5e9);"></div>
                            </div>
                            <div class="dept-percent">52%</div>
                        </div>
                        <div class="dept-bar">
                            <div class="dept-name">R&D</div>
                            <div class="dept-progress">
                                <div class="dept-fill" style="width: 24%; background: linear-gradient(90deg, #a855f7, #ec4899);"></div>
                            </div>
                            <div class="dept-percent">24%</div>
                        </div>
                        <div class="dept-bar">
                            <div class="dept-name">제조/기술</div>
                            <div class="dept-progress">
                                <div class="dept-fill" style="width: 24%; background: linear-gradient(90deg, #10b981, #059669);"></div>
                            </div>
                            <div class="dept-percent">24%</div>
                        </div>
                    </div>

                    <div class="session-composition">
                        <div class="session-title">4회차 (9.2-3)</div>
                        <div class="session-topic">AI X 차세대 NAND</div>
                        <div class="dept-bar">
                            <div class="dept-name">R&D</div>
                            <div class="dept-progress">
                                <div class="dept-fill" style="width: 29%; background: linear-gradient(90deg, #a855f7, #ec4899);"></div>
                            </div>
                            <div class="dept-percent">29%</div>
                        </div>
                        <div class="dept-bar">
                            <div class="dept-name">사업전략</div>
                            <div class="dept-progress">
                                <div class="dept-fill" style="width: 24%; background: linear-gradient(90deg, #06b6d4, #0ea5e9);"></div>
                            </div>
                            <div class="dept-percent">24%</div>
                        </div>
                        <div class="dept-bar">
                            <div class="dept-name">제조/기술</div>
                            <div class="dept-progress">
                                <div class="dept-fill" style="width: 18%; background: linear-gradient(90deg, #10b981, #059669);"></div>
                            </div>
                            <div class="dept-percent">18%</div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="chart-grid">
                <div class="chart-container">
                    <div class="chart-title">직군별 참여 추이</div>
                    <canvas id="departmentTrendChart"></canvas>
                </div>
                <div class="chart-container">
                    <div class="chart-title">경력별 참여 분포</div>
                    <canvas id="experienceTrendChart"></canvas>
                </div>
            </div>
        </div>

        <!-- 피드백 분석 탭 -->
        <div id="feedback" class="tab-content">
            <div class="wordcloud-container">
                <div class="chart-title">주관식 피드백 키워드 분석</div>
                <div class="session-filter">
                    <button class="filter-btn active" onclick="filterWordcloud('all')">전체</button>
                    <button class="filter-btn" onclick="filterWordcloud('1')">1회차</button>
                    <button class="filter-btn" onclick="filterWordcloud('2')">2회차</button>
                    <button class="filter-btn" onclick="filterWordcloud('3')">3회차</button>
                    <button class="filter-btn" onclick="filterWordcloud('4')">4회차</button>
                </div>
                <canvas id="wordcloud" width="800" height="300"></canvas>
            </div>

            <div class="sentiment-dashboard">
                <div class="sentiment-card positive">
                    <div class="sentiment-header">
                        <div class="sentiment-icon">😊</div>
                        <div class="sentiment-title">긍정적 피드백</div>
                    </div>
                    <div class="sentiment-count" style="color: #10b981;">87건 (74%)</div>
                    <div class="sentiment-examples">
                        "매우 만족", "유익한 시간", "도움이 되었습니다", "훌륭한 강의", "인사이트 향상"
                    </div>
                </div>

                <div class="sentiment-card neutral">
                    <div class="sentiment-header">
                        <div class="sentiment-icon">😐</div>
                        <div class="sentiment-title">중립적 피드백</div>
                    </div>
                    <div class="sentiment-count" style="color: #f59e0b;">21건 (18%)</div>
                    <div class="sentiment-examples">
                        "적당한 난이도", "보통", "괜찮았습니다", "무난했습니다"
                    </div>
                </div>

                <div class="sentiment-card negative">
                    <div class="sentiment-header">
                        <div class="sentiment-icon">😔</div>
                        <div class="sentiment-title">개선 요청</div>
                    </div>
                    <div class="sentiment-count" style="color: #ef4444;">10건 (8%)</div>
                    <div class="sentiment-examples">
                        "시간 부족", "어려웠다", "아쉬웠다", "접근성 문제", "화면 표시 요청"
                    </div>
                </div>
            </div>

            <div class="chart-grid">
                <div class="chart-container">
                    <div class="chart-title">회차별 감정 분석</div>
                    <canvas id="sentimentChart"></canvas>
                </div>
                <div class="chart-container">
                    <div class="chart-title">주요 요청 사항 분포</div>
                    <canvas id="requestChart"></canvas>
                </div>
            </div>

            <div class="insight-section">
                <div class="insight-title">피드백 인사이트</div>
                <div class="insight-grid">
                    <div class="insight-card">
                        <h4 data-icon="target">가장 많이 요청된 주제</h4>
                        <ul>
                            <li><span class="clickable" onclick="toggleDetail('quantum')">양자컴퓨팅 관련 기술 (12건)</span> <span style="color: #a855f7; cursor: pointer;">[상세보기]</span></li>
                            <li><span class="clickable" onclick="toggleDetail('ai-dc')">AI 데이터센터 및 발열 해결 (8건)</span> <span style="color: #a855f7; cursor: pointer;">[상세보기]</span></li>
                            <li><span class="clickable" onclick="toggleDetail('memory')">차세대 메모리 기술 (7건)</span> <span style="color: #a855f7; cursor: pointer;">[상세보기]</span></li>
                            <li><span class="clickable" onclick="toggleDetail('future')">반도체 미래 전망 (6건)</span> <span style="color: #a855f7; cursor: pointer;">[상세보기]</span></li>
                        </ul>
                        <div id="quantum" class="request-detail">
                            <h5>양자컴퓨팅 상세 요청</h5>
                            <ul>
                                <li>"양자컴퓨터 상용화 기술" (3건)</li>
                                <li>"양자컴퓨팅 생태계와 반도체 산업 역할" (2건)</li>
                                <li>"하이닉스의 양자컴퓨팅 메모리 시장 대비" (2건)</li>
                                <li>"양자 컴퓨터가 어느 산업까지 침투 가능한지" (3건)</li>
                                <li>"기존 chip/Memory업계는 어떤 영향을 받는지" (2건)</li>
                            </ul>
                        </div>
                        <div id="ai-dc" class="request-detail">
                            <h5>AI 데이터센터/발열 해결 상세 요청</h5>
                            <ul>
                                <li>"AI 데이터센터 구축 시 전력 포함 에너지 활용" (2건)</li>
                                <li>"서버 및 system에 대한 cooling system" (2건)</li>
                                <li>"칩 단위에서의 발열제어 (냉각 제외)" (1건)</li>
                                <li>"액침냉각" (1건)</li>
                                <li>"AI 데이터센터의 미래" (1건)</li>
                                <li>"발열 해결 관련 기술" (1건)</li>
                            </ul>
                        </div>
                        <div id="memory" class="request-detail">
                            <h5>차세대 메모리 기술 상세 요청</h5>
                            <ul>
                                <li>"차세대 메모리 기술" (2건)</li>
                                <li>"차세대 메모리 제품" (1건)</li>
                                <li>"미래 NAND 반도체" (1건)</li>
                                <li>"새로운 AI향 메모리의 평가(디램과 낸드가 아닌)" (1건)</li>
                                <li>"온디바이스향 특화 Custom Memory" (1건)</li>
                                <li>"Memory centric system 구현" (1건)</li>
                            </ul>
                        </div>
                        <div id="future" class="request-detail">
                            <h5>반도체 미래 전망 상세 요청</h5>
                            <ul>
                                <li>"미래 반도체 산업에 대해" (1건)</li>
                                <li>"반도체의 향후 발전상" (1건)</li>
                                <li>"환경 친화적인 관점에서의 next chip 방향" (1건)</li>
                                <li>"차세대 반도체는 어떻게 진화되는지" (1건)</li>
                                <li>"반도체의 미래에서 시너지 날 수 있는 사업분야" (1건)</li>
                                <li>"소버린 AI" (1건)</li>
                            </ul>
                        </div>
                    </div>
                    <div class="insight-card">
                        <h4 data-icon="gear">주요 개선 포인트</h4>
                        <ul>
                            <li>질의응답 시간 확대 (5건)</li>
                            <li>지역별 접근성 개선 (3건)</li>
                            <li>화면 표시 개선 (3건)</li>
                            <li>강의자료 사전 배포 (2건)</li>
                        </ul>
                    </div>
                    <div class="insight-card">
                        <h4 data-icon="lightbulb">만족 요인</h4>
                        <ul>
                            <li>전문가 구성의 우수성</li>
                            <li>최신 기술 트렌드 제공</li>
                            <li>이해하기 쉬운 설명</li>
                            <li>기술 인사이트 향상에 도움</li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>

        <!-- 전략적 인사이트 탭 -->
        <div id="insights" class="tab-content">
            <div class="education-overview">
                <div class="education-title">Next Chip Talk 교육 개요</div>
                <div class="education-grid">
                    <div class="education-item">
                        <h4>🎯 교육 목적</h4>
                        <p>급변하는 반도체 패러다임에 대응하기 위하여 근미래에 상용화될 가능성이 높은 반도체 기술을 조망하고, 최신 연구 동향과 기술적 난제에 대한 이해를 높여 기술 인사이트 향상을 목표로 함.</p>
                    </div>
                    <div class="education-item">
                        <h4>👥 수강 대상</h4>
                        <p>반도체 관련 멤버사의 기술/개발 및 전략/마케팅 구성원, 반도체 신기술 및 신사업에 대한 기술 동향 지식이 필요한 구성원 (기본적인 반도체 공정 기술에 대한 이해 필요)</p>
                    </div>
                    <div class="education-item">
                        <h4>📚 학습 방식</h4>
                        <ul>
                            <li>현장 참여 세미나</li>
                            <li>온라인 생중계를 통한 실시간 웨비나</li>
                            <li>추후 동영상 mySUNI 플랫폼에 녹화본 업로드</li>
                        </ul>
                    </div>
                    <div class="education-item">
                        <h4>🎬 학습 구성</h4>
                        <ul>
                            <li>모더레이터의 주제 키노트</li>
                            <li>전문가 강연 (학계 + 산업계)</li>
                            <li>대담과 질의 응답</li>
                        </ul>
                    </div>
                </div>
            </div>

            <div class="insight-section">
                <div class="insight-title">HRD 기반 교육 전략</div>
                <div class="insight-grid">
                    <div class="insight-card">
                        <h4 data-icon="growth">참가자 확보 전략</h4>
                        <ul>
                            <li>타겟 직군별 맞춤 마케팅 (R&D 40%, 사업전략 35%)</li>
                            <li>시즌별 참여도 분석 반영 (가을철 참여도 하락 대응)</li>
                            <li>조직의 Needs와 고객의 Wants를 반영하기 위한 정기적 고객 조사 실시</li>
                            <li>다양한 기업문화와 학습 선호도를 고려한 참여 확산 전략</li>
                        </ul>
                    </div>
                    <div class="insight-card">
                        <h4 data-icon="target">기술 인사이트 강화</h4>
                        <ul>
                            <li>양자컴퓨팅 전문 세션 신설 (수요 35% 반영)</li>
                            <li>AI 데이터센터 심화 과정 (발열/냉각 기술 포함)</li>
                            <li>차세대 메모리 기술 시리즈 구성</li>
                            <li>기술 트렌드 감각 향상 중심 콘텐츠</li>
                        </ul>
                    </div>
                    <div class="insight-card">
                        <h4 data-icon="gear">운영 혁신</h4>
                        <ul>
                            <li>실시간 Q&A 화면 표시 시스템 도입</li>
                            <li>지역별 접근성 개선 (청주, 이천 고려)</li>
                            <li>강의자료 사전/사후 제공 체계</li>
                            <li>질의응답 시간 30% 확대 (현재 + 추가 30분)</li>
                        </ul>
                    </div>
                    <div class="insight-card">
                        <h4 data-icon="money">ROI 평가 체계</h4>
                        <ul>
                            <li>Kirkpatrick-Phillips 5단계 모델 기반 체계적 평가</li>
                            <li>직접비용(강사료, 운영비) 대비 간접효과(업무생산성, 혁신창출) 측정</li>
                            <li>참가자 교육 전후 성과 변화 추적 시스템 구축</li>
                            <li>장기 누적효과 극대화를 위한 3년 단위 평가 계획</li>
                        </ul>
                    </div>
                    <div class="insight-card">
                        <h4 data-icon="loop">지속가능성 확보</h4>
                        <ul>
                            <li>기술 전문가 네트워킹 플랫폼 구축</li>
                            <li>분기별 기술 동향 레포트 제공</li>
                            <li>mySUNI 커뮤니티 기반 후속 스터디 도입</li>
                        </ul>
                    </div>
                </div>
            </div>

            <div class="chart-container">
                <div class="chart-title">Kirkpatrick-Phillips 5단계 평가 및 목표</div>
                <canvas id="kirkpatrickChart"></canvas>
                
                <div style="margin-top: 30px; padding: 25px; background: rgba(255, 255, 255, 0.06); border-radius: 12px; border-left: 4px solid #a855f7;">
                    <h4 style="color: #a855f7; margin-bottom: 15px; font-weight: 600;">HRD 평가 모델 기반 교육 효과성 분석</h4>
                    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px;">
                        <div>
                            <h5 style="color: #ffffff; margin-bottom: 10px; font-size: 0.95rem;">Level 1-2: 반응 및 학습</h5>
                            <p style="color: #d1d5db; font-size: 0.9rem; line-height: 1.5;">
                                참가자 만족도 4.5/5점, 추천률 95.1%로 교육에 대한 즉각적 반응이 매우 긍정적. 
                                기술 이해도 향상과 새로운 지식 습득이 효과적으로 이루어짐.
                            </p>
                        </div>
                        <div>
                            <h5 style="color: #ffffff; margin-bottom: 10px; font-size: 0.95rem;">Level 3: 행동 변화 (인사이트)</h5>
                            <p style="color: #d1d5db; font-size: 0.9rem; line-height: 1.5;">
                                참가자들의 기술 트렌드 감각 향상과 업무 접근 방식 개선이 관찰됨. 
                                후속 연구 및 프로젝트 기획에 교육 내용이 반영되는 사례 증가.
                            </p>
                        </div>
                        <div>
                            <h5 style="color: #ffffff; margin-bottom: 10px; font-size: 0.95rem;">Level 4-5: 결과 및 ROI</h5>
                            <p style="color: #d1d5db; font-size: 0.9rem; line-height: 1.5;">
                                기술 인사이트 향상을 통한 혁신 프로젝트 발굴과 의사결정 품질 개선. 
                                교육 투자 대비 조직 성과 창출 효과가 지속적으로 증가하는 추세.
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script>
        // 탭 전환 함수
        function showTab(tabName) {
            const tabs = document.querySelectorAll('.tab-content');
            const navTabs = document.querySelectorAll('.nav-tab');
            
            tabs.forEach(tab => tab.classList.remove('active'));
            navTabs.forEach(tab => tab.classList.remove('active'));
            
            document.getElementById(tabName).classList.add('active');
            event.target.classList.add('active');
        }

        // 상세 내용 토글 함수
        function toggleDetail(id) {
            const detail = document.getElementById(id);
            const allDetails = document.querySelectorAll('.request-detail');
            
            // 다른 모든 상세 내용 닫기
            allDetails.forEach(d => {
                if (d.id !== id) d.classList.remove('active');
            });
            
            // 클릭한 항목 토글
            detail.classList.toggle('active');
        }

        // 차트 데이터
        const chartData = {
            sessions: ['1회차\n(4.18)\nOptical', '2회차\n(6.25)\nGlass', '3회차\n(7.30)\nAI Chip', '4회차\n(9.2-3)\nNAND'],
            participants: [38, 38, 25, 17],
            satisfaction: [4.5, 4.6, 4.4, 4.5],
            recommendation: [95.0, 97.4, 100.0, 88.2],
            rdRatio: [45, 25, 24, 29],
            strategyRatio: [35, 50, 52, 24],
            techRatio: [20, 25, 24, 18]
        };

        // 워드클라우드 데이터
        const wordcloudData = {
            all: [
                ['양자컴퓨팅', 25], ['AI', 23], ['데이터센터', 18], ['차세대', 16], ['메모리', 15],
                ['반도체', 14], ['기술', 13], ['NAND', 12], ['유리기판', 11], ['발열', 10],
                ['NPU', 9], ['광통신', 8], ['미래', 8], ['시스템', 7], ['패키징', 6],
                ['소재', 6], ['냉각', 5], ['아키텍처', 5], ['엔비디아', 4], ['트렌드', 4]
            ],
            1: [['광통신', 15], ['차세대', 12], ['메모리', 10], ['포토닉스', 8], ['CXL', 6], ['PiM', 6], ['발열', 5], ['냉각', 5], ['양자', 4], ['환경', 3]],
            2: [['유리기판', 18], ['하이브리드본딩', 8], ['시스템반도체', 7], ['액침냉각', 6], ['양자컴퓨팅', 6], ['데이터센터', 5], ['ESG', 4], ['AI', 4], ['발열', 3]],
            3: [['AI', 20], ['메모리', 15], ['NPU', 12], ['차세대반도체', 8], ['Custom', 6], ['소부장', 5], ['Foundation', 4], ['시스템', 4], ['HW', 3], ['SW', 3]],
            4: [['NAND', 15], ['AI', 12], ['미래기술', 8], ['신소재', 6], ['미국반도체', 5], ['중국산업', 4], ['시장전망', 4], ['고객변화', 3], ['엔비디아', 3]]
        };

        // 차트 기본 설정
        Chart.defaults.font.family = "'Noto Sans KR', sans-serif";
        Chart.defaults.color = '#ffffff';

        // 만족도 차트
        new Chart(document.getElementById('satisfactionChart'), {
            type: 'line',
            data: {
                labels: chartData.sessions,
                datasets: [{
                    label: '만족도',
                    data: chartData.satisfaction,
                    borderColor: '#a855f7',
                    backgroundColor: 'rgba(168, 85, 247, 0.2)',
                    borderWidth: 4,
                    fill: true,
                    tension: 0.4,
                    pointBackgroundColor: '#a855f7',
                    pointBorderColor: '#fff',
                    pointBorderWidth: 3,
                    pointRadius: 8,
                    pointHoverRadius: 10
                }]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: { display: false }
                },
                scales: {
                    y: { 
                        beginAtZero: true,
                        max: 5,
                        ticks: { color: '#ffffff', font: { size: 12 } },
                        grid: { color: 'rgba(255, 255, 255, 0.1)' }
                    },
                    x: {
                        ticks: { color: '#ffffff', font: { size: 11 } },
                        grid: { color: 'rgba(255, 255, 255, 0.1)' }
                    }
                }
            }
        });

        // 추천률 차트
        new Chart(document.getElementById('recommendationChart'), {
            type: 'bar',
            data: {
                labels: chartData.sessions,
                datasets: [{
                    label: '추천률 (%)',
                    data: chartData.recommendation,
                    backgroundColor: [
                        '#a855f7',
                        '#ec4899',
                        '#06b6d4',
                        '#10b981'
                    ],
                    borderRadius: 12,
                    borderSkipped: false,
                    borderWidth: 2,
                    borderColor: [
                        '#d8b4fe',
                        '#f9a8d4',
                        '#67e8f9',
                        '#6ee7b7'
                    ]
                }]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: { display: false }
                },
                scales: {
                    y: { 
                        beginAtZero: true,
                        max: 100,
                        ticks: { color: '#ffffff', font: { size: 12 } },
                        grid: { color: 'rgba(255, 255, 255, 0.1)' }
                    },
                    x: {
                        ticks: { color: '#ffffff', font: { size: 11 } },
                        grid: { color: 'rgba(255, 255, 255, 0.1)' }
                    }
                }
            }
        });

        // 직군별 참여 추이 차트
        new Chart(document.getElementById('departmentTrendChart'), {
            type: 'line',
            data: {
                labels: chartData.sessions,
                datasets: [{
                    label: 'R&D',
                    data: chartData.rdRatio,
                    borderColor: '#a855f7',
                    backgroundColor: 'rgba(168, 85, 247, 0.2)',
                    tension: 0.4,
                    borderWidth: 3,
                    pointRadius: 6
                }, {
                    label: '사업전략',
                    data: chartData.strategyRatio,
                    borderColor: '#06b6d4',
                    backgroundColor: 'rgba(6, 182, 212, 0.2)',
                    tension: 0.4,
                    borderWidth: 3,
                    pointRadius: 6
                }, {
                    label: '제조/기술',
                    data: chartData.techRatio,
                    borderColor: '#10b981',
                    backgroundColor: 'rgba(16, 185, 129, 0.2)',
                    tension: 0.4,
                    borderWidth: 3,
                    pointRadius: 6
                }]
            },
            options: {
                responsive: true,
                scales: {
                    y: { 
                        beginAtZero: true,
                        max: 60,
                        ticks: { color: '#ffffff', font: { size: 12 } },
                        grid: { color: 'rgba(255, 255, 255, 0.1)' }
                    },
                    x: {
                        ticks: { color: '#ffffff', font: { size: 11 } },
                        grid: { color: 'rgba(255, 255, 255, 0.1)' }
                    }
                },
                plugins: {
                    legend: {
                        labels: { color: '#ffffff', font: { size: 12 } }
                    }
                }
            }
        });

        // 경력별 참여 분포 차트
        new Chart(document.getElementById('experienceTrendChart'), {
            type: 'doughnut',
            data: {
                labels: ['10년 이상', '5-10년', '5년 미만'],
                datasets: [{
                    data: [71.2, 18.5, 10.3],
                    backgroundColor: ['#a855f7', '#ec4899', '#06b6d4'],
                    borderWidth: 3,
                    borderColor: '#0f0f23'
                }]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: { 
                        position: 'bottom',
                        labels: { padding: 25, color: '#ffffff', font: { size: 12 } }
                    }
                }
            }
        });

        // 감정 분석 차트
        new Chart(document.getElementById('sentimentChart'), {
            type: 'bar',
            data: {
                labels: chartData.sessions,
                datasets: [{
                    label: '긍정',
                    data: [85, 92, 78, 65],
                    backgroundColor: '#10b981'
                }, {
                    label: '중립',
                    data: [12, 6, 18, 25],
                    backgroundColor: '#f59e0b'
                }, {
                    label: '개선요청',
                    data: [3, 2, 4, 10],
                    backgroundColor: '#ef4444'
                }]
            },
            options: {
                responsive: true,
                scales: {
                    x: { 
                        stacked: true,
                        ticks: { color: '#ffffff', font: { size: 11 } },
                        grid: { color: 'rgba(255, 255, 255, 0.1)' }
                    },
                    y: { 
                        stacked: true,
                        ticks: { color: '#ffffff', font: { size: 12 } },
                        grid: { color: 'rgba(255, 255, 255, 0.1)' }
                    }
                },
                plugins: {
                    legend: {
                        labels: { color: '#ffffff', font: { size: 12 } }
                    }
                }
            }
        });

        // 요청 사항 분포 차트
        new Chart(document.getElementById('requestChart'), {
            type: 'doughnut',
            data: {
                labels: ['양자컴퓨팅', 'AI/데이터센터', '차세대 메모리', '발열 해결', '기타'],
                datasets: [{
                    data: [35, 25, 20, 15, 5],
                    backgroundColor: ['#a855f7', '#ec4899', '#06b6d4', '#10b981', '#f59e0b'],
                    borderWidth: 3,
                    borderColor: '#0f0f23'
                }]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: { 
                        position: 'bottom',
                        labels: { padding: 20, color: '#ffffff', font: { size: 12 } }
                    }
                }
            }
        });

        // Kirkpatrick 차트
        new Chart(document.getElementById('kirkpatrickChart'), {
            type: 'radar',
            data: {
                labels: ['Level1\n반응', 'Level2\n학습', 'Level3\n인사이트', 'Level4\n결과', 'Level5\nROI'],
                datasets: [{
                    label: '현재 수준',
                    data: [95, 83, 75, 60, 75],
                    borderColor: '#a855f7',
                    backgroundColor: 'rgba(168, 85, 247, 0.3)',
                    borderWidth: 3,
                    pointRadius: 6
                }, {
                    label: '2025 목표',
                    data: [98, 90, 85, 80, 85],
                    borderColor: '#ec4899',
                    backgroundColor: 'rgba(236, 72, 153, 0.2)',
                    borderWidth: 3,
                    borderDash: [8, 5],
                    pointRadius: 6
                }]
            },
            options: {
                responsive: true,
                scales: {
                    r: {
                        beginAtZero: true,
                        max: 100,
                        ticks: { color: '#ffffff', font: { size: 11 } },
                        grid: { color: 'rgba(255, 255, 255, 0.3)' },
                        pointLabels: { color: '#ffffff', font: { size: 12 } }
                    }
                },
                plugins: {
                    legend: {
                        labels: { color: '#ffffff', font: { size: 12 } }
                    }
                }
            }
        });

        // 워드클라우드 생성 함수
        function generateWordcloud(data) {
            const canvas = document.getElementById('wordcloud');
            const ctx = canvas.getContext('2d');
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            
            if (typeof WordCloud !== 'undefined') {
                WordCloud(canvas, {
                    list: data,
                    gridSize: Math.round(18 * canvas.width / 1024),
                    weightFactor: function (size) {
                        return Math.pow(size, 2.2) * canvas.width / 1024;
                    },
                    fontFamily: "'Noto Sans KR', sans-serif",
                    color: function (word, weight) {
                        const colors = ['#a855f7', '#ec4899', '#06b6d4', '#10b981', '#f59e0b'];
                        return colors[Math.floor(Math.random() * colors.length)];
                    },
                    rotateRatio: 0.4,
                    rotationSteps: 2,
                    backgroundColor: 'transparent'
                });
            } else {
                // WordCloud 라이브러리가 로드되지 않은 경우 대체 텍스트 표시
                ctx.font = '24px "Noto Sans KR"';
                ctx.fillStyle = '#a855f7';
                ctx.textAlign = 'center';
                ctx.fillText('워드클라우드 로딩 중...', canvas.width/2, canvas.height/2);
            }
        }

        // 워드클라우드 필터링 함수
        function filterWordcloud(session) {
            const buttons = document.querySelectorAll('.filter-btn');
            buttons.forEach(btn => btn.classList.remove('active'));
            event.target.classList.add('active');
            
            const data = wordcloudData[session] || wordcloudData.all;
            generateWordcloud(data);
        }

        // 초기 워드클라우드 생성
        setTimeout(() => {
            generateWordcloud(wordcloudData.all);
        }, 1000);
    </script>
</body>
</html>
