from io import StringIO
import pandas as pd

# ALIO 사이트의 수입/지출 데이터 (HTML 테이블 원본 요약)
html_data = """
<table border="1">
<thead>
<tr>
<th>구분</th>
<th>2020년 결산</th>
<th>2021년 결산</th>
<th>2022년 결산</th>
<th>2023년 결산</th>
<th>2024년 결산</th>
<th>2025년 예산</th>
</tr>
</thead>
<tbody>
<tr>
<td>수입합계</td>
<td>226,944</td>
<td>240,240</td>
<td>255,638</td>
<td>262,625</td>
<td>267,224</td>
<td>266,049</td>
</tr>
<tr>
<td>지출합계</td>
<td>230,744</td>
<td>243,957</td>
<td>265,577</td>
<td>276,671</td>
<td>275,796</td>
<td>266,049</td>
</tr>
</tbody>
</table>
"""

# HTML을 데이터프레임으로 변환
df = pd.read_html(StringIO(html_data))[0]

# '구분' 컬럼을 인덱스로 설정 (수입합계, 지출합계 행을 식별하기 위함)
df.set_index('구분', inplace=True)

# 행과 열을 바꿈 (연도가 행으로 오도록)
df = df.T

# 컬럼 이름 깔끔하게 정리
df.columns = ['수입', '지출']
df.index.name = '연도'

# CSV 파일로 저장
df.to_csv("연도별 수입 및 지출 현황.csv", encoding="utf-8-sig")

print("작업 완료! 아래는 저장된 데이터 내용입니다.")
print(df)
