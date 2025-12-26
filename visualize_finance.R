# visualize_finance.R

# 1. 필요한 패키지 설치 및 로드
# renv 환경이 활성화되어 있으므로 해당 프로젝트 라이브러리에 설치됩니다.
required_packages <- c("ggplot2", "tidyr", "readr")

for (pkg in required_packages) {
  if (!requireNamespace(pkg, quietly = TRUE)) {
    message(paste("Installing package:", pkg))
    install.packages(pkg, repos = "https://cloud.r-project.org")
  }
}

library(ggplot2)
library(tidyr)
library(readr)

# 2. 데이터 읽기
# read_csv는 기본적으로 UTF-8을 잘 처리하지만, Windows에서 생성된 CSV가 CP949일 경우를 대비해
# locale(encoding = "UTF-8") 또는 "CP949" 지정을 고려할 수 있습니다.
# 여기서는 표준적인 처리를 시도합니다.
csv_file <- "연도별 수입 및 지출 현황.csv"
if (!file.exists(csv_file)) {
  stop("CSV 파일이 존재하지 않습니다.")
}

df <- read_csv(csv_file, show_col_types = FALSE)

# 3. 데이터 변환 (Wide -> Long)
df_long <- pivot_longer(df, cols = c("수입", "지출"), names_to = "구분", values_to = "금액")

# 4. 그래프 그리기
p <- ggplot(df_long, aes(x = 연도, y = 금액, fill = 구분)) +
  geom_bar(stat = "identity", position = "dodge") +
  labs(title = "연도별 수입 및 지출 현황", x = "연도", y = "금액") +
  theme_minimal() +
  theme(text = element_text(family = "Malgun Gothic")) # Windows 한글 폰트 설정

# 5. 그래프 저장
ggsave("finance_graph_r.png", plot = p, width = 10, height = 6, dpi = 300)

message("그래프가 finance_graph_r.png 파일로 저장되었습니다.")
