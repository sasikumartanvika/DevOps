import calendar
from datetime import datetime

now = datetime.now()

year = now.year
month = now.month
month_name = now.strftime("%B")

cal = calendar.HTMLCalendar(firstweekday=0)
calendar_html = cal.formatmonth(year, month)

html = f"""
<!DOCTYPE html>
<html>
<head>
    <title>My Calendar</title>

    <style>
        body {{
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            text-align: center;
            padding: 40px;
        }}

        .container {{
            background: white;
            color: #333;
            max-width: 700px;
            margin: auto;
            padding: 30px;
            border-radius: 20px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        }}

        h1 {{
            color: #667eea;
        }}

        table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }}

        th {{
            background: #667eea;
            color: white;
            padding: 12px;
        }}

        td {{
            padding: 15px;
            border: 1px solid #ddd;
        }}

        td:hover {{
            background: #e8eaff;
            color: #667eea;
            font-weight: bold;
        }}

        .footer {{
            margin-top: 20px;
            color: #777;
        }}
    </style>
</head>

<body>

<div class="container">

    <h1>📅 My Calendar</h1>

    <h2>{month_name} {year}</h2>

    {calendar_html}

    <div class="footer">
        Generated using Python 🐍 and Docker 🐳
    </div>

</div>

</body>
</html>
"""

with open("index.html", "w") as file:
    file.write(html)

print("Webpage generated successfully!")
