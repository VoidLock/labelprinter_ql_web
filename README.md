## labelprinter\_ql\_web

This is a web service to print labels on QL label printers.

You need Python 3 for this software to work.

![Screenshot](./static/images/screenshots/Label-Designer_Desktop.png)

The web interface is [responsive](https://en.wikipedia.org/wiki/Responsive_web_design).
There's also a screenshot showing [how it looks on a smartphone](./static/images/screenshots/Label-Designer_Phone.png)

## Printer Support

This application supports two types of label printers:
- **Brother QL Series**: QL-500, QL-550, QL-560, QL-570, QL-580N, QL-650TD, QL-700, QL-710W, QL-720NW, QL-1050, QL-1060N
- **DYMO LabelWriter Series**: LabelWriter 450 (and compatible models)

You can switch between printer types by modifying the `config.json` configuration file.

### Installation

**ProTip™**: If you know how to use Docker, you might want to use my ready-to-use Docker image to deploy this software.
It can be found [on the Docker hub](https://hub.docker.com/r/pklaus/brother_ql_web/).  
Otherwise, follow the instructions below.

Get the code:

    git clone https://github.com/pklaus/brother_ql_web.git

or download [the ZIP file](https://github.com/pklaus/brother_ql_web/archive/master.zip) and unpack it.

Install the requirements:

    pip install -r requirements.txt

**For DYMO LabelWriter support**, also install the required library for DataMatrix barcode generation (used in Grocy webhook integration):

    pip install pylibdmtx

In addition, `fontconfig` should be installed on your system. It's used to identify and
inspect fonts on your machine. This package is pre-installed on many Linux distributions.
If you're using a Mac, I recommend to use [Homebrew](https://brew.sh) to install
fontconfig using [`brew install fontconfig`](http://brewformulas.org/Fontconfig).

### Configuration file

Copy `config.example.json` to `config.json` (e.g. `cp config.example.json config.json`) and adjust the values to match your needs.

#### Brother QL Configuration Example

```json
{
  "SERVER": {
    "PORT": 8013,
    "HOST": "",
    "LOGLEVEL": "WARNING"
  },
  "PRINTER": {
    "TYPE": "brother_ql",
    "MODEL": "QL-700",
    "PRINTER": "file:///dev/usb/lp0"
  },
  "LABEL": {
    "DEFAULT_SIZE": "62",
    "DEFAULT_ORIENTATION": "standard"
  }
}
```

#### DYMO LabelWriter Configuration Example

```json
{
  "SERVER": {
    "PORT": 8013,
    "HOST": "",
    "LOGLEVEL": "WARNING"
  },
  "PRINTER": {
    "TYPE": "dymo",
    "MODEL": "LabelWriter-450",
    "PRINTER": "DYMO LabelWriter 450"
  },
  "LABEL": {
    "DEFAULT_SIZE": "30252",
    "DEFAULT_ORIENTATION": "standard"
  },
  "WEBSITE": {
    "PAGE_TITLE": "DYMO Label Designer"
  }
}
```

**Note**: For DYMO printers, the `PRINTER` field can be:
- A CUPS printer name (e.g., `"DYMO LabelWriter 450"`)
- A file path (e.g., `"file:///dev/usb/lp0"`)
- The application will use CUPS for printing on Linux systems

### Startup

To start the server, run `./labelprinter_ql_web.py`. The command line parameters overwrite the values configured in `config.json`. Here's its command line interface:

    usage: labelprinter_ql_web.py [-h] [--port PORT] [--loglevel LOGLEVEL]
                             [--font-folder FONT_FOLDER]
                             [--default-label-size DEFAULT_LABEL_SIZE]
                             [--default-orientation {standard,rotated}]
                             [--model MODEL]
                             [--printer-type {brother_ql,dymo}]
                             [printer]
    
    This is a web service to print labels on QL label printers.
    
    positional arguments:
      printer               String descriptor for the printer to use (like
                            tcp://192.168.0.23:9100 or file:///dev/usb/lp0)
    
    optional arguments:
      -h, --help            show this help message and exit
      --port PORT
      --loglevel LOGLEVEL
      --font-folder FONT_FOLDER
                            folder for additional .ttf/.otf fonts
      --default-label-size DEFAULT_LABEL_SIZE
                            Label size inserted in your printer. 
                            For Brother QL, defaults to 62.
                            For DYMO, use label part numbers like 30252.
      --default-orientation {standard,rotated}
                            Label orientation, defaults to "standard". To turn
                            your text by 90°, state "rotated".
      --model MODEL         The model of your printer 
                            (e.g., QL-700 for Brother QL, LabelWriter-450 for DYMO)
      --printer-type {brother_ql,dymo}
                            Type of printer: brother_ql or dymo

**Examples**:

Brother QL printer:
```bash
./labelprinter_ql_web.py --printer-type brother_ql --model QL-700 file:///dev/usb/lp0
```

DYMO LabelWriter printer:
```bash
./labelprinter_ql_web.py --printer-type dymo --model LabelWriter-450 "DYMO LabelWriter 450"
```

### Usage

Once it's running, access the web interface by opening the page with your browser.
If you run it on your local machine, go to <http://localhost:8013> (You can change
the default port 8013 using the --port argument).
You will then be forwarded by default to the interactive web gui located at `/labeldesigner`.

All in all, the web server offers:

* a Web GUI allowing you to print your labels at `/labeldesigner`,
* an API at `/api/print/text?text=Your_Text&font_size=100&font_family=Minion%20Pro%20(%20Semibold%20)`
  to print a label containing 'Your Text' with the specified font properties.
* a Grocy webhook endpoint at `/api/print/grocy` for printing product labels with DataMatrix barcodes

### DYMO Label Sizes

The following DYMO label sizes are supported:

#### High Priority (Common Grocy Use Cases)
- `30252` / `99010`: 28mm x 89mm Address labels
- `30334` / `11354`: 57mm x 32mm Return address labels  
- `11352`: 25mm x 54mm Return address labels
- `99012`: 36mm x 89mm Large address labels
- `99014`: 54mm x 101mm Shipping address labels

#### Medium Priority
- `11353`: 13mm x 25mm Multipurpose labels
- `11355`: 19mm x 51mm Return address labels
- `30258`: 54mm x 70mm Multipurpose labels
- `30332`: 25mm x 25mm Square labels (for small items)
- `99015`: 54mm x 70mm Name badge labels

#### Lower Priority
- `11356`: 41mm x 89mm Name badge labels
- `30256`: 59mm x 102mm Address labels
- `30327`: 14mm x 87mm File folder labels
- `30374`: 51mm x 89mm Name badge labels
- `30376`: 14mm x 51mm Hanging folder labels
- `30856`: 62mm x 106mm Name badge labels
- `30915`: 41mm x 31mm Postage stamp labels
- `99013`: 36mm x 89mm Large address labels (transparent plastic)
- `99017`: 12mm x 50mm Hanging folder labels
- `99019`: 59mm x 190mm Lever arch labels

### Grocy Webhook Integration

Both Brother QL and DYMO printers support the Grocy webhook for printing product labels with DataMatrix barcodes.

**Endpoint**: `POST /api/print/grocy`

**Parameters**:
- `product`: Product name (required)
- `grocycode`: DataMatrix barcode content (required)
- `duedate`: Expiration/due date (optional)

**Example configuration in Grocy**:
1. Go to Grocy settings → Label printer
2. Set webhook URL: `http://your-server:8013/api/print/grocy`
3. Configure the webhook to send product name, grocy code, and due date

The webhook will automatically:
- Generate a DataMatrix barcode from the grocycode
- Format the label with product name and optional due date
- Print to your configured printer (Brother QL or DYMO)

### License

This software is published under the terms of the GPLv3, see the LICENSE file in the repository.

Parts of this package are redistributed software products from 3rd parties. They are subject to different licenses:

* [Bootstrap](https://github.com/twbs/bootstrap), MIT License
* [Glyphicons](https://getbootstrap.com/docs/3.3/components/#glyphicons), MIT License (as part of Bootstrap 3.3)
* [jQuery](https://github.com/jquery/jquery), MIT License
