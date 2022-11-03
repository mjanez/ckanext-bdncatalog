[![Tests](https://github.com/mjanez/ckanext-bdncatalog/workflows/Tests/badge.svg?branch=main)](https://github.com/mjanez/ckanext-bdncatalog/actions)

# ckanext-bdncatalog

**TODO:** Put a description of your extension here:  What does it do? What features does it have? Consider including some screenshots or embedding a video!


## Requirements

**TODO:** For example, you might want to mention here which versions of CKAN this
extension works with.

If your extension works across different versions you can add the following table:

Compatibility with core CKAN versions:

| CKAN version    | Compatible?   |
| --------------- | ------------- |
| 2.6 and earlier | not tested    |
| 2.7             | not tested    |
| 2.8             | not tested    |
| 2.9             | not tested    |

Suggested values:

* "yes"
* "not tested" - I can't think of a reason why it wouldn't work
* "not yet" - there is an intention to get it working
* "no"


## Installation

**TODO:** Add any additional install steps to the list below.
   For example installing any non-Python dependencies or adding any required
   config settings.

To install ckanext-bdncatalog:

1. Activate your CKAN virtual environment, for example:

     . /usr/lib/ckan/default/bin/activate

2. Clone the source and install it on the virtualenv
	```
	git clone https://github.com/mjanez/ckanext-bdncatalog.git
	cd ckanext-bdncatalog
	pip install -e .
	pip install -r requirements.txt
	```
3. Add `bdncatalog` to the `ckan.plugins` setting in your CKAN
   config file (by default the config file is located at
   `/etc/ckan/default/ckan.ini`).

4. Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu:

     sudo service apache2 reload


## Config settings

None at present

**TODO:** Document any optional config settings here. For example:

	# The minimum number of hours to wait before re-checking a resource
	# (optional, default: 24).
	ckanext.bdncatalog.some_setting = some_default_value


## Developer installation

To install ckanext-bdncatalog for development, activate your CKAN virtualenv and
do:

    git clone https://github.com/mjanez/ckanext-bdncatalog.git
    cd ckanext-bdncatalog
    python setup.py develop
    pip install -r dev-requirements.txt


## Tests

To run the tests, do:

    pytest --ckan-ini=test.ini


## Releasing a new version of ckanext-bdncatalog

If ckanext-bdncatalog should be available on PyPI you can follow these steps to publish a new version:

1. Update the version number in the `setup.py` file. See [PEP 440](http://legacy.python.org/dev/peps/pep-0440/#public-version-identifiers) for how to choose version numbers.

2. Make sure you have the latest version of necessary packages:

    pip install --upgrade setuptools wheel twine

3. Create a source and binary distributions of the new version:

       python setup.py sdist bdist_wheel && twine check dist/*

   Fix any errors you get.

4. Upload the source distribution to PyPI:

       twine upload dist/*

5. Commit any outstanding changes:

       git commit -a
       git push

6. Tag the new release of the project on GitHub with the version number from
   the `setup.py` file. For example if the version number in `setup.py` is
   0.0.1 then do:

       git tag 0.0.1
       git push --tags


## Load TTLs
Ad-hoc CKAN software to retrieve data from EIDOS TTL and ingest datasets into CKAN.

**Requeriments:**
The code compiles with Python 3. The required libraries can be found in `requirements.txt`.

### Configuration
The necessary steps to configure the environment and install the libraries are as follows. First create the `venv` directory where it will run (or replace `whoami` with the desired user name if you create for example one for `ckan`):
```bash
# Linux
cd /my/path
python3 -m venv .env    # sudo apt-get install python3-venv
. my/path/.env/bin/activate
python3 -m pip install  install -r requirements.txt

# Windows
cd /my/path
python -m venv .env
my/path/.env/Scripts/activate.bat  # CMD || env\Scripts\Activate.ps1  # Powershell
pip install  install -r requirements.txt
```

### Launch
1. Download https://datos.iepnb.es/datasets/eidos.ttl
	```bash
	curl -o eidos.ttl https://datos.iepnb.es/datasets/eidos.ttl
	```
2. Update `splitFilesEidosTTL.py` parameters:
	- `ckan_url`: CKAN site.
	- `path_orig`: Folder of EIDOS complete TTL.
	- `path_tmp`: Temp folder for TTLs

2. Execute splitFilesEidosTTL:
	```bash
	python3 splitFilesEidosTTL.py
	```
3. Create a `eidos-prueba` organization in CKAN.
4. Update `loadEidosTTL.py` parameters:
	- `ckan_url`: CKAN site.
	- `api_key`: http://{ckan_site_url}:5000/user/admin authorization key.
	- `path_tmp`: SplitFilesEidosTTL.py `path_tmp`
	
5. Load TTLs into CKAN
	```bash
	python3 loadEidosTTL.py
	```

### Sample:
**Darwin_Location100422.ttl**
```json
{
   "owner_org":"eidos-prueba",
   "type":"location",
   "Plinian_hasCell":[
      "https://datos.iepnb.es/recurso/sector-publico/cuadricula-espacial/celda/10kmE384N189"
   ],
   "Plinian_isLocationOf":[
      "https://datos.iepnb.es/recurso/sector-publico/medio-ambiente/pliniancore/TaxonRecord/20075",
      "https://datos.iepnb.es/recurso/sector-publico/medio-ambiente/pliniancore/TaxonRecord/20082",
      "https://datos.iepnb.es/recurso/sector-publico/medio-ambiente/pliniancore/TaxonRecord/20092"
   ],
   "title":"10kmE384N189",
   "name":"location_10kme384n189",
   "uri":"https://datos.iepnb.es/recurso/sector-publico/medio-ambiente/pliniancore/Location/10kmE384N189",
   "Darwin_locationID":[
      "10kmE384N189"
   ]
}
```
>**Note**<br>
> `Inserted location` - https://datos.iepnb.es/recurso/sector-publico/medio-ambiente/pliniancore/Location/10kmE384N189


## License

[AGPL](https://www.gnu.org/licenses/agpl-3.0.en.html)
