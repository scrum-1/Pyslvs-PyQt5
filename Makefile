all: build run

#Windows: Temporarily display log for debugging.
build: launch_pyslvs.py
	@echo ---Pyslvs  Build---
ifeq ($(OS),Windows_NT)
	@echo ---Windows Version---
	pyinstaller launch_pyslvs.py -i ./icons/main_big.ico
	python setup.py build
	@echo ---Copying Folder and Files---
	xcopy .\build\exe.win-amd64-3.5\core\kernel\py35w .\dist\launch_pyslvs\core\kernel\py35w /s /y /i
	xcopy .\build\exe.win-amd64-3.5\core\kernel\pyslvs_generate\py35w .\dist\launch_pyslvs\core\kernel\pyslvs_generate\py35w /s /y /i
	rename .\dist\launch_pyslvs Pyslvs
else
	@echo ---Linux Version---
	pyinstaller launch_pyslvs.py
	mv dist/launch_pyslvs dist/Pyslvs
endif
	@echo ---Done---

run: build dist/Pyslvs
ifeq ($(OS),Windows_NT)
	@dist/Pyslvs/launch_pyslvs.exe
else
	@dist/Pyslvs/launch_pyslvs
endif

DEBIANCONTROL = dist/Pyslvs/DEBIAN/control

deb: build dist/Pyslvs
ifeq ($(OS),Windows_NT)
	@echo ---Ubuntu only---
else
	mkdir dist/Pyslvs/DEBIAN
	touch $(DEBIANCONTROL)
	echo 'Package: Pyslvs' >> $(DEBIANCONTROL)
	echo 'Version: 0.6.1' >> $(DEBIANCONTROL)
	echo 'Architecture: all' >> $(DEBIANCONTROL)
	echo 'Description: Dimensional Synthesis of Planar Four-bar Linkages in PyQt5 GUI.' >> $(DEBIANCONTROL)
	echo 'Maintainer: Yuan Chang <daan0014119@gmail.com>' >> $(DEBIANCONTROL)
	dpkg -b dist/Pyslvs
endif

clean:
ifeq ($(OS),Windows_NT)
	rd build /s /q
	rd dist /s /q
	del launch_pyslvs.spec
else
	rm -f -r build
	rm -f -r dist
	rm -f launch_pyslvs.spec
endif
