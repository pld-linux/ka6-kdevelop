#
# Conditional build:
%bcond_with	tests		# build with tests
%bcond_without	webengine	# build without webengine

%define		kdeappsver	24.08.0
%define		kframever	5.103.0
%define		qtver		5.15.2
%define		kaname		kdevelop

%ifarch x32
%undefine with_webengine
%endif

Summary:	KDE Integrated Development Environment
Summary(de.UTF-8):	KDevelop ist eine grafische Entwicklungsumgebung für KDE
Summary(pl.UTF-8):	Zintegrowane środowisko programisty dla KDE
Summary(pt_BR.UTF-8):	Ambiente Integrado de Desenvolvimento para o KDE
Summary(zh_CN.UTF-8):	KDE C/C++集成开发环境
Name:		ka6-kdevelop
Version:	24.08.0
Release:	1
License:	GPL
Group:		X11/Development/Tools
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	ff7ea78e109655d30d50b16fef7fc28b
URL:		http://www.kdevelop.org/
BuildRequires:	Qt6Help-devel >= %{qtver}
%{?with_webengine:BuildRequires:	Qt6WebEngine-devel >= %{qtver}}
BuildRequires:	astyle-devel >= 3.1
BuildRequires:	clang-devel
BuildRequires:	clang-tools-extra
BuildRequires:	cmake >= 3.20
BuildRequires:	docbook-dtd45-xml
BuildRequires:	docbook-style-xsl
BuildRequires:	gettext-tools
#BuildRequires:	ka5-okteta-devel >= 1:0.26.9-3
BuildRequires:	ka6-kdevelop-pg-qt >= 2.3.0
BuildRequires:	ka6-libkomparediff2-devel
BuildRequires:	kf6-kcrash-devel >= %{kframever}
BuildRequires:	kf6-kdoctools-devel >= %{kframever}
BuildRequires:	kf6-krunner-devel >= %{kframever}
BuildRequires:	kf6-syntax-highlighting-devel >= %{kframever}
BuildRequires:	kf6-threadweaver-devel >= %{kframever}
BuildRequires:	kp6-libksysguard-devel
BuildRequires:	llvm-mlir-devel
BuildRequires:	qt6-assistant >= %{qtver}

BuildRequires:	libstdc++-devel >= 3.3
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.600
BuildRequires:	zlib-devel >= 1.2.0
BuildConflicts:	star
Requires:	%{name}-data = %{version}-%{release}
Requires:	libstdc++-gdb
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	shared-mime-info
Obsoletes:	ka5-%{kaname} < %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqfiles .*\\.zshrc

%description
The KDevelop Integrated Development Environment provides many features
that developers need as well as providing a unified interface to
programs like gdb, the C/C++ compiler, and make.

KDevelop manages or provides: all development tools needed for C++
programming like Compiler, Linker, automake and autoconf; KAppWizard,
which generates complete, ready-to-go sample applications;
Classgenerator, for creating new classes and integrating them into the
current project; File management for sources, headers, documentation
etc. to be included in the project; The creation of User-Handbooks
written with SGML and the automatic generation of HTML-output with the
KDE look and feel; Automatic HTML-based API-documentation for your
project's classes with cross-references to the used libraries;
Internationalization support for your application, allowing
translators to easily add their target language to a project;

KDevelop also includes WYSIWYG (What you see is what you get)-creation
of user interfaces with a built-in dialog editor; Debugging your
application by integrating KDbg; Editing of project-specific pixmaps
with KIconEdit; The inclusion of any other program you need for
development by adding it to the "Tools"-menu according to your
individual needs.

%description -l de.UTF-8
KDevelop ist eine grafische Entwicklungsumgebung für KDE.

Das KDevelop-Projekt wurde 1998 begonnen, um eine einfach zu
bedienende grafische (integrierte) Entwicklungsumgebung für C++ und C
auf Unix-basierten Betriebssystemen bereitzustellen. Seit damals ist
die KDevelop-IDE öffentlich unter der GPL erhältlich und unterstützt
u. a. Qt-, KDE-, GNOME-, C++- und C-Projekte.

%description -l pl.UTF-8
KDevelop to zintegrowane środowisko programistyczne dla KDE, dające
wiele możliwości przydatnych programistom oraz zunifikowany interfejs
do programów typu gdb, kompilator C/C++ oraz make.

KDevelop obsługuje lub zawiera: wszystkie narzędzia programistyczne
potrzebne do programowania w C++ jak kompilator, linker, automake,
autoconf; KAppWizard, generujący kompletne, gotowe do uruchomienia,
proste aplikacje; Classgenerator do tworzenia nowych klas i włączania
ich do projektu; zarządzanie plikami źródłowymi, nagłówkowymi,
dokumentacją itp.; tworzenie podręczników użytkownika pisanych w SGML
i automatyczne generowanie wyjścia HTML pasującego do KDE;
automatyczne tworzenie dokumentacji API w HTML do klas projektu z
odniesieniami do używanych bibliotek; wsparcie dla
internacjonalizacji, pozwalające tłumaczom łatwo dodawać pliki z
tłumaczeniami do projektu.

KDevelop ma także tworzenie interfejsów użytkownika przy użyciu
edytora dialogów WYSIWYG; odpluskwianie aplikacji poprzez integrację z
KDbg; edycję ikon przy pomocy KIconEdit; dołączanie innych programów
potrzebnych do programowania przez dodanie ich do menu Tools według
własnych potrzeb.

%package data
Summary:	Data files for %{kaname}
Summary(pl.UTF-8):	Dane dla %{kaname}
Group:		X11/Development/Tools
Requires:	filesystem >= 4.1-18
Obsoletes:	bash-completion-kdevelop <= 23.08.4-1
Obsoletes:	ka5-%{kaname}-data < %{version}
BuildArch:	noarch

%description data
Data files for %{kaname}.

%description data -l pl.UTF-8
Dane dla %{kaname}.

%package devel
Summary:	kdevelop - header files and development documentation
Summary(pl.UTF-8):	kdevelop - pliki nagłówkowe i dokumentacja
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	ka5-%{kaname}-devel < %{version}

%description devel
This package contains header files and development documentation for
kdevelop.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki nagłówkowe i dokumentację potrzebną przy
pisaniu własnych programów wykorzystujących kdevelop.

%prep
%setup -q -n %{kaname}-%{version}

%build
%cmake \
	-B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_DOCBUNDLEDIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DFORCE_BASH_COMPLETION_INSTALLATION=ON
%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%update_mime_database
%update_desktop_database

%postun
/sbin/ldconfig
%update_mime_database
%update_desktop_database_postun

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kdevelop
%attr(755,root,root) %{_bindir}/kdevelop!
%attr(755,root,root) %{_bindir}/kdev_includepathsconverter
%attr(755,root,root) %{_libdir}/libKDevClangPrivate.so.*
%attr(755,root,root) %{_libdir}/libKDevCMakeCommon.so.*
%attr(755,root,root) %{_libdir}/libKDevCompileAnalyzerCommon.so.*
%attr(755,root,root) %{_libdir}/libKDevelopSessionsWatch.so
%dir %{_libdir}/qt6/plugins/kf6/krunner
%dir %{_libdir}/qt6/qml/org/kde/plasma/private/kdevelopsessions
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/plasma/private/kdevelopsessions/libkdevelopsessionsplugin.so
%{_libdir}/qt6/qml/org/kde/plasma/private/kdevelopsessions/qmldir

#kdevplatform
%attr(755,root,root) %{_bindir}/kdev_dbus_socket_transformer
%attr(755,root,root) %{_bindir}/kdev_format_source
%attr(755,root,root) %{_bindir}/kdevplatform_shell_environment.sh
%attr(755,root,root) %{_libdir}/libKDevPlatformDocumentation.so.*.*.*
%attr(755,root,root) %{_libdir}/libKDevPlatformInterfaces.so.*.*.*
%attr(755,root,root) %{_libdir}/libKDevPlatformLanguage.so.*.*.*
%attr(755,root,root) %{_libdir}/libKDevPlatformOutputView.so.*.*.*
%attr(755,root,root) %{_libdir}/libKDevPlatformProject.so.*.*.*
%attr(755,root,root) %{_libdir}/libKDevPlatformSerialization.so.*.*.*
%attr(755,root,root) %{_libdir}/libKDevPlatformShell.so.*.*.*
%attr(755,root,root) %{_libdir}/libKDevPlatformSublime.so.*.*.*
%attr(755,root,root) %{_libdir}/libKDevPlatformUtil.so.*.*.*
%attr(755,root,root) %{_libdir}/libKDevPlatformVcs.so.*.*.*
%attr(755,root,root) %{_libdir}/libKDevPlatformDebugger.so.*.*
%ghost %{_libdir}/libKDevPlatformDebugger.so.??
%ghost %{_libdir}/libKDevPlatformDocumentation.so.??
%ghost %{_libdir}/libKDevPlatformInterfaces.so.??
%ghost %{_libdir}/libKDevPlatformLanguage.so.??
%ghost %{_libdir}/libKDevPlatformOutputView.so.??
%ghost %{_libdir}/libKDevPlatformProject.so.??
%ghost %{_libdir}/libKDevPlatformSerialization.so.??
%ghost %{_libdir}/libKDevPlatformShell.so.??
%ghost %{_libdir}/libKDevPlatformSublime.so.??
%ghost %{_libdir}/libKDevPlatformUtil.so.??
%ghost %{_libdir}/libKDevPlatformVcs.so.??
%dir %{_libdir}/qt6/plugins/kdevplatform
%dir %{_libdir}/qt6/plugins/kdevplatform/60
%attr(755,root,root) %{_libdir}/qt6/plugins/kdevplatform/60/KDevCMakeManager.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kdevplatform/60/KDevCustomBuildSystem.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kdevplatform/60/KDevCustomMakeManager.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kdevplatform/60/KDevDefinesAndIncludesManager.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kdevplatform/60/KDevGenericManager.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kdevplatform/60/KDevMakeBuilder.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kdevplatform/60/KDevManPage.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kdevplatform/60/KDevMesonManager.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kdevplatform/60/KDevNinjaBuilder.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kdevplatform/60/KDevOutlineView.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kdevplatform/60/KDevProjectFilter.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kdevplatform/60/KDevProjectManagerView.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kdevplatform/60/KDevQMakeBuilder.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kdevplatform/60/KDevQMakeManager.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kdevplatform/60/KDevStandardOutputView.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kdevplatform/60/KDevWelcomePage.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kdevplatform/60/kdevandroid.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kdevplatform/60/kdevappwizard.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kdevplatform/60/kdevastyle.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kdevplatform/60/kdevbazaar.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kdevplatform/60/kdevclangsupport.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kdevplatform/60/kdevclangtidy.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kdevplatform/60/kdevclassbrowser.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kdevplatform/60/kdevclazy.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kdevplatform/60/kdevcodeutils.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kdevplatform/60/kdevcontextbrowser.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kdevplatform/60/kdevcppcheck.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kdevplatform/60/kdevcraft.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kdevplatform/60/kdevcustomscript.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kdevplatform/60/kdevdocker.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kdevplatform/60/kdevdocumentswitcher.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kdevplatform/60/kdevdocumentview.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kdevplatform/60/kdevexecute.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kdevplatform/60/kdevexecuteplasmoid.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kdevplatform/60/kdevexecutescript.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kdevplatform/60/kdevexternalscript.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kdevplatform/60/kdevfilemanager.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kdevplatform/60/kdevfiletemplates.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kdevplatform/60/kdevflatpak.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kdevplatform/60/kdevgdb.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kdevplatform/60/kdevghprovider.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kdevplatform/60/kdevgit.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kdevplatform/60/kdevgrepview.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kdevplatform/60/kdevheaptrack.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kdevplatform/60/kdevkonsoleview.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kdevplatform/60/kdevlldb.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kdevplatform/60/kdevopenwith.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kdevplatform/60/kdevpatchreview.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kdevplatform/60/kdevperforce.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kdevplatform/60/kdevproblemreporter.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kdevplatform/60/kdevqthelp.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kdevplatform/60/kdevquickopen.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kdevplatform/60/kdevsourceformatter.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kdevplatform/60/kdevswitchtobuddy.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kdevplatform/60/kdevtestview.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kdevplatform/60/kdevvcschangesviewplugin.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kdevplatform/60/scratchpad.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kdevplatform/60/KDevCMakeBuilder.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kdevplatform/60/KDevCMakeDocumentation.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/krunner/kdevelopsessions.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/ktexttemplate/kdev_filters.so

%files data -f %{kaname}.lang
%defattr(644,root,root,755)
%{bash_compdir}/kdevelop
%dir %{_datadir}/kdevplatform
%dir %{_datadir}/kdevplatform/shellutils
%{_datadir}/kdevplatform/shellutils/.zshrc
%{_datadir}/kdevappwizard
%{_datadir}/kdevclangsupport
%{_datadir}/kdevelop
%{_datadir}/kdevfiletemplates
%{_datadir}/kdevgdb
%{_datadir}/kdevlldb
%{_datadir}/kdevmanpage
%{_datadir}/knsrcfiles/kdev*.knsrc
%{_datadir}/metainfo/*
%{_datadir}/mime/packages/*
%{_desktopdir}/org.kde.kdevelop.desktop
%{_desktopdir}/org.kde.kdevelop_*.desktop
%{_iconsdir}/*/*x*/*/*.png
%{_datadir}/kdevcodegen
%{_datadir}/kdevcodeutils
%{_iconsdir}/hicolor/*/actions/*.svg
%{_iconsdir}/hicolor/*/apps/*.svg
%{_datadir}/knotifications6/kdevelop.notifyrc
%dir %{_datadir}/plasma/plasmoids/org.kde.kdevelopsessions
%dir %{_datadir}/plasma/plasmoids/org.kde.kdevelopsessions/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.kdevelopsessions/contents/ui
%{_datadir}/plasma/plasmoids/org.kde.kdevelopsessions/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.kdevelopsessions/metadata.json
%{_datadir}/qlogging-categories6/kdevelop.categories
%{_datadir}/qlogging-categories6/kdevplatform.categories

%files devel
%defattr(644,root,root,755)
%{_libdir}/cmake/KDevelop
%{_includedir}/kdevelop

#kdevplatform
%{_includedir}/kdevplatform
%{_libdir}/libKDevPlatformDebugger.so
%{_libdir}/libKDevPlatformDocumentation.so
%{_libdir}/libKDevPlatformInterfaces.so
%{_libdir}/libKDevPlatformLanguage.so
%{_libdir}/libKDevPlatformOutputView.so
%{_libdir}/libKDevPlatformProject.so
%{_libdir}/libKDevPlatformSerialization.so
%{_libdir}/libKDevPlatformShell.so
%{_libdir}/libKDevPlatformSublime.so
%{_libdir}/libKDevPlatformUtil.so
%{_libdir}/libKDevPlatformVcs.so
%dir %{_libdir}/cmake/KDevPlatform
%{_libdir}/cmake/KDevPlatform/KDevPlatformConfig.cmake
%{_libdir}/cmake/KDevPlatform/KDevPlatformConfigVersion.cmake
%{_libdir}/cmake/KDevPlatform/KDevPlatformMacros.cmake
%{_libdir}/cmake/KDevPlatform/KDevPlatformTargets.cmake
%{_libdir}/cmake/KDevPlatform/KDevPlatformTargets-pld.cmake
