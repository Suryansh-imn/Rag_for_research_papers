from app.pdf_loader import extract_text

text = extract_text("papers/personalized-antibiograms-for-machine-learning-driven-19uvhsdj.pdf")

print(text[:5000])