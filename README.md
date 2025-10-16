# Translation Loop

This Python script allows you to extract text from a PDF file, translate it into your desired language using [translators](https://github.com/UlionTse/translators), and save the translated text back into a new PDF file. The script supports customization of the translator service, translation chunk size, output file name, and delay between translation API requests.

## Features

- **Extracts text** from a PDF using `pdfplumber`
- **Translates text** with the `translators` library (default: Yandex, supports many others)
- **Customizable translation** settings (language, chunk size, delay, translator service)
- **Saves translated text** into a new PDF with proper formatting using `reportlab`
- **Simple GUI prompt** for selecting the input PDF file

## Requirements

Install dependencies with pip:

```
pip install pdfplumber translators reportlab
```

> **Note:** If you encounter issues with `translators`, check the [official repo](https://github.com/UlionTse/translators) for troubleshooting and updates.

## Usage

You will be prompted to:

1. **Select the PDF** you want to translate.
2. **Enter the output PDF filename** (including `.pdf` extension).
3. **Choose the translator** (default: `yandex`).
4. **Set the delay** between translation requests (default: `3` seconds).
5. **Specify the target language code** (default: `en` for English).
6. **Set the character limit per chunk** (default: `3800`).

The script will extract text, split it into manageable chunks, translate each chunk, and save the translated content to your specified output PDF.

## Example

```
Enter output PDF file name (with .pdf extension): output_translated.pdf
Choose translator (default: yandex): google
Enter delay between requests in seconds (default: 3): 2
Enter target language code (default: en): fr
Enter character limit per chunk (default: 3800): 3500
```

## Customization

- **Translator service:** You can use other supported services such as `google`, `bing`, `deepl`, etc.
- **Language codes:** Use standard language codes like `en` (English), `fr` (French), `es` (Spanish), etc.
- **Chunk size:** Adjust if you encounter issues with long texts or rate-limiting.
- **Delay:** Increase if you hit rate limits on the translation service.

## Limitations

- The translation quality and speed depend on the chosen service and its current API restrictions.
- PDF formatting is basic; complex layouts are not preserved.
- Large PDFs may take longer due to API rate limits.

## License

MIT

## Credits

- [pdfplumber](https://github.com/jsvine/pdfplumber)
- [translators](https://github.com/UlionTse/translators)
- [reportlab](https://github.com/Helios42/ReportLab)
