import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import platform

# 1. CSV 파일 읽기
df = pd.read_csv("연도별 수입 및 지출 현황.csv")

# '연도' 컬럼을 인덱스로 설정 (만약 CSV에 '연도' 컬럼이 있다면)
if '연도' in df.columns:
    df.set_index('연도', inplace=True)

# 2. 한글 폰트 설정 (Windows 환경)
if platform.system() == 'Windows':
    font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
    rc('font', family=font_name)
else:
    # Mac이나 다른 환경일 경우 대비 (기본설정)
    plt.rc('font', family='AppleGothic')

# 마이너스 기호 깨짐 방지
plt.rcParams['axes.unicode_minus'] = False

# 3. 막대 그래프 그리기
ax = df.plot(kind='bar', figsize=(10, 6), rot=0)

# 4. 그래프 꾸미기
plt.title('연도별 수입 및 지출 현황')
plt.xlabel('연도')
plt.ylabel('금액 (단위: 백만원)')
plt.legend(['수입', '지출'])
plt.grid(axis='y', linestyle='--', alpha=0.7)

# 5. 그래프 저장 및 출력
output_file = "finance_graph.png"
plt.savefig(output_file)
print(f"그래프가 '{output_file}' 파일로 저장되었습니다.")

# 팝업으로 보여주기 (환경에 따라 안 뜰 수도 있음)
try:
    plt.show()
except:
    pass
