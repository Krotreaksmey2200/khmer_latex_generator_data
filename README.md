# Khmer Math Dataset Generator (High Performance)

កម្មវិធីសម្រាប់បង្កើត Dataset អត្ថបទខ្មែរ លាយជាមួយសមីការគណិតវិទ្យា (LaTeX) ក្នុងទម្រង់ជារូបភាព និងអត្ថបទ (.tsv) សម្រាប់យកទៅប្រើប្រាស់ក្នុងវិស័យ AI និង Data Science។

## មុខងារសំខាន់ៗ (Features)

*   **AI Generation:** ប្រើប្រាស់ Gemini 2.0 Flash ដើម្បីបង្កើតអត្ថបទខ្មែរ និងរូបមន្ត LaTeX ដោយស្វ័យប្រវត្តិតាមប្រធានបទដែលអ្នកចង់បាន។
*   **High Performance:** ដំណើរការដោយប្រព័ន្ធ Multi-threading (Parallel Processing) អាចបង្កើតរូបភាពច្រើនក្នុងពេលតែមួយយ៉ាងរហ័ស។
*   **Manual Batch Mode:** អាចបញ្ចូលកូដ LaTeX ច្រើនបន្ទាត់ដើម្បីបម្លែងជារូបភាពជាក្រុមៗ (១ បន្ទាត់ = ១ រូបភាព)។
*   **Duplicate Detection:** ប្រព័ន្ធពិនិត្យទិន្នន័យជាន់គ្នាដោយស្វ័យប្រវត្តិ ដើម្បីធានាថាទិន្នន័យនីមួយៗក្នុង Dataset មិនមានការស្ទួនគ្នា។
*   **Output Management:** អាចជ្រើសរើសទីតាំងរក្សាទុក (Folder) និងដាក់ឈ្មោះ Dataset បានតាមចិត្ត។
*   **Settings Persistence:** រក្សាទុក API Key និងការកំណត់ផ្សេងៗដោយស្វ័យប្រវត្តិ (Settings.json)។
*   **Modern GUI:** ចំណុចប្រទាក់ស្អាត ងាយស្រួលប្រើប្រាស់ ជាមួយ Dashboard បង្ហាញស្ថិតិជោគជ័យ និង Log ដំណើរការ។

## តម្រូវការប្រព័ន្ធ (Prerequisites)

មុននឹងដំណើរការកម្មវិធី អ្នកត្រូវប្រាកដថាបានដំឡើង៖

1.  **Python 3.10+**
2.  **XeLaTeX:** សម្រាប់ចងក្រងអត្ថបទខ្មែរ (មានក្នុង TeX Live ឬ MiKTeX)។
3.  **Poppler:** សម្រាប់បម្លែង PDF ទៅជារូបភាព (ដំឡើងតាមរយៈ `brew install poppler` លើ Mac ឬតាមរយៈតំណភ្ជាប់ផ្លូវការលើ Windows)។
4.  **Khmer Fonts:** ដំឡើង Font "Noto Serif Khmer" ឬ "Khmer OS Content"។

## ការដំឡើង (Installation)

១. បង្កើត Virtual Environment (ស្រេចចិត្ត):
```bash
python -m venv gen_data
source gen_data/bin/activate  # សម្រាប់ Mac/Linux
gen_data\Scripts\activate     # សម្រាប់ Windows
```

២. ដំឡើងបណ្ណាល័យដែលចាំបាច់:
```bash
pip install customtkinter google-generativeai pdf2image pillow
```

## របៀបប្រើប្រាស់ (Usage)

១. ដំណើរការកម្មវិធី:
```bash
python app.py
```

២. បញ្ចូល **Google AI API Key** (យកពី Google AI Studio)។
៣. ចុច **Auto-Detect Models** ដើម្បីជ្រើសរើស Gemini Model ដែលស័ក្តិសម។
៤. កំណត់ទីតាំងរក្សាទុកក្នុងប្រអប់ **Output Folder**។
៥. កំណត់ចំនួនទិន្នន័យដែលចង់បង្កើត រួចចុច **Start Processing**។

## រចនាសម្ព័ន្ធគម្រោង (Project Structure)

*   `app.py`: កម្មវិធី GUI និង Logic ចម្បង។
*   `generator.py`: ផ្នែកទាក់ទងជាមួយ Gemini AI។
*   `latex_engine.py`: ផ្នែកបម្លែងអត្ថបទទៅជា PDF តាមរយៈ XeLaTeX។
*   `pdf_converter.py`: ផ្នែកបម្លែង PDF ទៅជារូបភាព JPG។
*   `dataset_writer.py`: ផ្នែកកត់ត្រាទិន្នន័យចូលក្នុង file .tsv។
*   `settings.json`: ឯកសាររក្សាទុកការកំណត់របស់អ្នក។

## អ្នកអភិវឌ្ឍន៍
បង្កើតឡើងដោយក្តីស្រឡាញ់ សម្រាប់ការរីកចម្រើននៃវិស័យទិន្នន័យអក្សរសាស្ត្រខ្មែរ។
