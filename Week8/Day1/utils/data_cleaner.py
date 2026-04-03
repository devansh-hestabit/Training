import pandas as pd
import json
import random
from pathlib import Path
from transformers import AutoTokenizer
import matplotlib.pyplot as plt
import numpy as np

BASE_DIR = Path(__file__).resolve().parent.parent
RAW_PATH = BASE_DIR / "data" / "raw" / "WA_Fn-UseC_-HR-Employee-Attrition.csv"
CLEAN_PATH = BASE_DIR / "data" / "clean.jsonl"
TRAIN_PATH = BASE_DIR / "data" / "train.jsonl"
VAL_PATH = BASE_DIR / "data" / "val.jsonl"

TRAIN_RATIO = 0.9
SEED = 42
MIN_TOTAL_TOKENS = 10
MAX_TOTAL_TOKENS = 128

tokenizer = AutoTokenizer.from_pretrained("gpt2")

def count_tokens(text: str) -> int:
    return len(tokenizer.encode(text, add_special_tokens=False))

def load_jsonl(path):
    with open(path, "r", encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]

def save_jsonl(data, path):
    with open(path, "w", encoding="utf-8") as f:
        for sample in data:
            f.write(json.dumps(sample, ensure_ascii=False) + "\n")

df = pd.read_csv(RAW_PATH)
df.drop_duplicates(inplace=True)
df.dropna(inplace=True)

df['Attrition'] = df['Attrition'].str.strip().str.title()
df['OverTime'] = df['OverTime'].str.strip().str.title()
df['Gender'] = df['Gender'].str.strip().str.title()
df['Department'] = df['Department'].str.strip().str.title()

constant_cols = [col for col in df.columns if df[col].nunique() == 1]
df.drop(columns=constant_cols, inplace=True)

dataset = []
for idx, row in df.iterrows():
    emp_id = row['EmployeeNumber']
    
    sample1 = {
        "instruction": "Answer this HR question about an employee",
        "input": f"Employee #{emp_id}: Age {row['Age']}, {row['Gender']}, {row['JobRole']}, Dept: {row['Department']}, Salary: ${row['MonthlyIncome']:,}, Satisfaction: {row['JobSatisfaction']}/5, Attrition: {row['Attrition']}",
        "output": f"Profile: {row['Gender']} {row['JobRole']} (age {row['Age']}) in {row['Department']} earns ${row['MonthlyIncome']:,}/month. Satisfaction: {row['JobSatisfaction']}/5. {'Left' if row['Attrition']=='Yes' else 'Stayed'}. {row['TotalWorkingYears']}yr exp."
    }
    dataset.append(sample1)
    
    sample2 = {
        "instruction": "Analyze employee attrition risk",
        "input": f"Emp #{emp_id}: {row['YearsAtCompany']}yr tenure, OverTime: {row['OverTime']}, Distance: {row['DistanceFromHome']}mi, JobLevel: {row['JobLevel']}, Outcome: {row['Attrition']}",
        "output": f"{'HIGH RISK→LEFT' if row['Attrition']=='Yes' else 'LOW RISK→STAYED'}. Factors: Short tenure ({row['YearsAtCompany']}yr), Overtime ({row['OverTime']}), Long commute ({row['DistanceFromHome']}mi), Level {row['JobLevel']}."
    }
    dataset.append(sample2)
    
    sample3 = {
        "instruction": "Extract key HR metrics from record",
        "input": f"Emp #{emp_id}: Dept={row['Department']}, Edu={row['Education']}, Level={row['JobLevel']}, Perf={row['PerformanceRating']}, Balance={row['WorkLifeBalance']}, Stock={row['StockOptionLevel']}",
        "output": json.dumps({
    "department": row["Department"],
    "education": int(row["Education"]),
    "job_level": int(row["JobLevel"]),
    "performance_rating": int(row["PerformanceRating"]),
    "work_life_balance": int(row["WorkLifeBalance"]),
    "stock_option_level": int(row["StockOptionLevel"])
})}
    dataset.append(sample3)

clean_data = []
for sample in dataset:
    total_tokens = (
        count_tokens(sample["instruction"]) +
        count_tokens(sample["input"]) +
        count_tokens(sample["output"])
    )
    if MIN_TOTAL_TOKENS <= total_tokens <= MAX_TOTAL_TOKENS:
        clean_data.append(sample)

random.seed(SEED)
random.shuffle(clean_data)

split_idx = int(len(clean_data) * TRAIN_RATIO)
train_data = clean_data[:split_idx]
val_data = clean_data[split_idx:]

save_jsonl(clean_data, CLEAN_PATH)
save_jsonl(train_data, TRAIN_PATH)
save_jsonl(val_data, VAL_PATH)


instruction_tokens = []
input_tokens = []
output_tokens = []
total_tokens = []

for sample in clean_data:
    it = count_tokens(sample["instruction"])
    ipt = count_tokens(sample["input"])
    ot = count_tokens(sample["output"])
    tt = it + ipt + ot

    instruction_tokens.append(it)
    input_tokens.append(ipt)
    output_tokens.append(ot)
    total_tokens.append(tt)

def print_stats(name, values):
    print(
        f"{name}: min={min(values)}, "
        f"max={max(values)}, "
        f"avg={np.mean(values):.2f}"
    )

print_stats("Instruction tokens", instruction_tokens)
print_stats("Input tokens", input_tokens)
print_stats("Output tokens", output_tokens)
print_stats("Total tokens", total_tokens)

FIG_DIR = BASE_DIR / "data" / "analysis"
FIG_DIR.mkdir(parents=True, exist_ok=True)

plt.figure(figsize=(8, 5))
plt.hist(total_tokens, bins=30)
plt.title("Total Token Length Distribution")
plt.xlabel("Total Tokens")
plt.ylabel("Number of Samples")
plt.tight_layout()

output_path = FIG_DIR / "total_token_distribution.png"
plt.savefig(output_path)
plt.close()
