%define guide_version 0.9.1-1
Summary:	Realistic sky generator
Summary(pl.UTF-8):	Realistyczny generator obrazu nieba
Name:		stellarium
Version:	0.10.0
Release:	3
License:	GPL v2
Group:		X11/Applications/Science
Source0:	http://dl.sourceforge.net/stellarium/%{name}-%{version}.tgz
# Source0-md5:	09465fa11a8caab7a4410f1e5ff6eb8c
Source1:	%{name}.desktop
Source2:	%{name}.png
Source3:	http://dl.sourceforge.net/stellarium/%{name}_user_guide-%{guide_version}.pdf
# Source3-md5:	0e708c4c0af77712c64b22cbfa398fb4
Patch0:		%{name}-po.patch
URL:		http://www.stellarium.org/
BuildRequires:	OpenGL-devel
BuildRequires:	QtGui-devel
BuildRequires:	QtOpenGL-devel
BuildRequires:	QtScript-devel
BuildRequires:	SDL_mixer-devel >= 1.2
BuildRequires:	boost-devel
BuildRequires:	cmake
BuildRequires:	curl-devel
BuildRequires:	freetype-devel
BuildRequires:	gettext-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libpng-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Stellarium renders 3D realistic skies in real time with OpenGL. It
displays stars, constellations, planets, nebulas and others things
like ground, landscape, fog, etc. Main features:
- Over 120000 stars from the Hipparcos Catalogue with name and infos
  for the brightest ones.
- Planets in real time, with a powerfull zoom mode.
- Drawing of the 88 constellations with their names.
- More than 40 messiers objects (Orion, M31 etc..).
- Photorealistic Milky Way.
- Ground, fog, and landscape.
- Star twinkling.
- Time control (real time and accelered time modes).
- Clikable stars, planets and nebulas with informations.
- Smooth real time navigation.
- Windowed and fullscreen modes.

%description -l pl.UTF-8
Stellarium przy pomocy OpenGL-a oddaje w czasie rzeczywistym
trójwymiarowe, realistyczne obrazy nieba. Wyświetla gwiazdy,
konstelacje, planety, mgławice i inne obiekty takie jak powierzchnia
ziemi, krajobrazy, mgła, itp. Główne cechy to:
- Ponad 120000 gwiazd z "Hipparcos Catalogue" z nazwami i opisem
  najjaśniejszych.
- Planety w czasie rzeczywistym z możliwością dużego powiększania.
- Wyświetlanie 88 konstelacji wraz z ich nazwami.
- Ponad 40 obiektów messiera (Orion, M31, itp...).
- Realistyczna Droga Mleczna.
- Powierzchnia, mgła i krajobraz.
- Migotanie gwiazd.
- Kontrola czasu (tryby czasu rzeczywistego i przyśpieszonego).
- Dostęp do informacji na temat gwiazd, planet i mgławic po ich
  kliknięciu.
- Płynna nawigacja w czasie rzeczywistym.
- Tryb pracy pełnoekranowej i w oknie.

%prep
%setup -q
%patch0 -p1
# bogus "Hawaiian" translation (English with some quirks and empty strings)
rm po/*/{haw,fil}.po

install %{SOURCE3} .

%build
%cmake \
        -DCMAKE_INSTALL_PREFIX=%{_prefix} \
        .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README %{name}_user_guide-%{guide_version}.pdf
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_mandir}/man1/%{name}.1*
%{_pixmapsdir}/%{name}.png
