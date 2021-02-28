#
# TODO:
#  - automate packaging all fancy translations
#
%define guide_version 1
Summary:	Realistic sky generator
Summary(pl.UTF-8):	Realistyczny generator obrazu nieba
Name:		stellarium
Version:	0.20.1
Release:	1
License:	GPL v2+
Group:		X11/Applications/Science
Source0:	https://github.com/Stellarium/stellarium/releases/download/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	19422ba4800fbede0a71a723cf3df10f
Source1:	https://github.com/Stellarium/stellarium/releases/download/v%{version}/%{name}_user_guide-%{version}-%{guide_version}.pdf
# Source1-md5:	7986c8f77fbf6e71872877eb878a492f
URL:		http://stellarium.org/
BuildRequires:	OpenGL-devel
BuildRequires:	Qt5Concurrent-devel
BuildRequires:	Qt5Declarative-devel
BuildRequires:	Qt5Gui-devel
BuildRequires:	Qt5Multimedia-devel
BuildRequires:	Qt5MultimediaWidgets-devel
BuildRequires:	Qt5Network-devel
BuildRequires:	Qt5OpenGL-devel
BuildRequires:	Qt5Positioning-devel
BuildRequires:	Qt5Script-devel
BuildRequires:	Qt5SerialPort-devel
BuildRequires:	Qt5Test-devel
BuildRequires:	boost-devel
BuildRequires:	cmake
BuildRequires:	curl-devel
BuildRequires:	freetype-devel
BuildRequires:	gettext-tools
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libpng-devel >= 2:1.2.0
BuildRequires:	perl-tools-pod
BuildRequires:	qt5-build
BuildRequires:	qt5-linguist
BuildRequires:	qt5-qmake
Requires:	%{name}-data = %{version}-%{release}
Requires:	Qt5Gui-platform-xcb-glx
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

%package data
Summary:	Stellarium data files
Group:		X11/Applications/Science
BuildArch:	noarch

%description data
Stellarium data files

%prep
%setup -q

install %{SOURCE1} .

%build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DBUILD_SHARED_LIBS=OFF \
	.

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CREDITS.md ChangeLog README.md %{name}_user_guide-%{version}-%{guide_version}.pdf
%attr(755,root,root) %{_bindir}/*
%{_datadir}/metainfo/stellarium.appdata.xml
%{_desktopdir}/%{name}.desktop
%{_mandir}/man1/%{name}.1*
%{_pixmapsdir}/%{name}.xpm
%{_iconsdir}/*/*/apps/stellarium.png

%files data
%defattr(644,root,root,755)
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/data
%{_datadir}/%{name}/landscapes
%{_datadir}/%{name}/models
%{_datadir}/%{name}/nebulae
%{_datadir}/%{name}/scenery3d
%{_datadir}/%{name}/scripts
%{_datadir}/%{name}/skycultures
%{_datadir}/%{name}/stars
%{_datadir}/%{name}/textures
%{_datadir}/%{name}/webroot
%{_datadir}/mime/packages/stellarium.xml
%dir %{_datadir}/%{name}/translations
%dir %{_datadir}/%{name}/translations/stellarium
%dir %{_datadir}/%{name}/translations/stellarium-planetary-features
%dir %{_datadir}/%{name}/translations/stellarium-remotecontrol
%dir %{_datadir}/%{name}/translations/stellarium-skycultures
%lang(af) %{_datadir}/%{name}/translations/stellarium-planetary-features/af.qm
%lang(ar) %{_datadir}/%{name}/translations/stellarium-planetary-features/ar.qm
%lang(ast) %{_datadir}/%{name}/translations/stellarium-planetary-features/ast.qm
%lang(az) %{_datadir}/%{name}/translations/stellarium-planetary-features/az.qm
%lang(be) %{_datadir}/%{name}/translations/stellarium-planetary-features/be.qm
%lang(bg) %{_datadir}/%{name}/translations/stellarium-planetary-features/bg.qm
%lang(bn) %{_datadir}/%{name}/translations/stellarium-planetary-features/bn.qm
%lang(br) %{_datadir}/%{name}/translations/stellarium-planetary-features/br.qm
%lang(bs) %{_datadir}/%{name}/translations/stellarium-planetary-features/bs.qm
%lang(ca) %{_datadir}/%{name}/translations/stellarium-planetary-features/ca.qm
%lang(ca@valencia) %{_datadir}/%{name}/translations/stellarium-planetary-features/ca@valencia.qm
%lang(cs) %{_datadir}/%{name}/translations/stellarium-planetary-features/cs.qm
%lang(cv) %{_datadir}/%{name}/translations/stellarium-planetary-features/cv.qm
%lang(da) %{_datadir}/%{name}/translations/stellarium-planetary-features/da.qm
%lang(de) %{_datadir}/%{name}/translations/stellarium-planetary-features/de.qm
%lang(el) %{_datadir}/%{name}/translations/stellarium-planetary-features/el.qm
%lang(en) %{_datadir}/%{name}/translations/stellarium-planetary-features/en.qm
%lang(en_AU) %{_datadir}/%{name}/translations/stellarium-planetary-features/en_AU.qm
%lang(en_CA) %{_datadir}/%{name}/translations/stellarium-planetary-features/en_CA.qm
%lang(en_GB) %{_datadir}/%{name}/translations/stellarium-planetary-features/en_GB.qm
%lang(en_US) %{_datadir}/%{name}/translations/stellarium-planetary-features/en_US.qm
%lang(eo) %{_datadir}/%{name}/translations/stellarium-planetary-features/eo.qm
%lang(es) %{_datadir}/%{name}/translations/stellarium-planetary-features/es.qm
%lang(et) %{_datadir}/%{name}/translations/stellarium-planetary-features/et.qm
%lang(eu) %{_datadir}/%{name}/translations/stellarium-planetary-features/eu.qm
%lang(fa) %{_datadir}/%{name}/translations/stellarium-planetary-features/fa.qm
%lang(fi) %{_datadir}/%{name}/translations/stellarium-planetary-features/fi.qm
%lang(fr) %{_datadir}/%{name}/translations/stellarium-planetary-features/fr.qm
%lang(fy) %{_datadir}/%{name}/translations/stellarium-planetary-features/fy.qm
%lang(ga) %{_datadir}/%{name}/translations/stellarium-planetary-features/ga.qm
%lang(gd) %{_datadir}/%{name}/translations/stellarium-planetary-features/gd.qm
%lang(gl) %{_datadir}/%{name}/translations/stellarium-planetary-features/gl.qm
%lang(gu) %{_datadir}/%{name}/translations/stellarium-planetary-features/gu.qm
%lang(he) %{_datadir}/%{name}/translations/stellarium-planetary-features/he.qm
%lang(hi) %{_datadir}/%{name}/translations/stellarium-planetary-features/hi.qm
%lang(hr) %{_datadir}/%{name}/translations/stellarium-planetary-features/hr.qm
%lang(hu) %{_datadir}/%{name}/translations/stellarium-planetary-features/hu.qm
%lang(hy) %{_datadir}/%{name}/translations/stellarium-planetary-features/hy.qm
%lang(id) %{_datadir}/%{name}/translations/stellarium-planetary-features/id.qm
%lang(is) %{_datadir}/%{name}/translations/stellarium-planetary-features/is.qm
%lang(it) %{_datadir}/%{name}/translations/stellarium-planetary-features/it.qm
%lang(ja) %{_datadir}/%{name}/translations/stellarium-planetary-features/ja.qm
%lang(jv) %{_datadir}/%{name}/translations/stellarium-planetary-features/jv.qm
%lang(ka) %{_datadir}/%{name}/translations/stellarium-planetary-features/ka.qm
%lang(kk) %{_datadir}/%{name}/translations/stellarium-planetary-features/kk.qm
%lang(ko) %{_datadir}/%{name}/translations/stellarium-planetary-features/ko.qm
%lang(ku) %{_datadir}/%{name}/translations/stellarium-planetary-features/ku.qm
%lang(ky) %{_datadir}/%{name}/translations/stellarium-planetary-features/ky.qm
%lang(la) %{_datadir}/%{name}/translations/stellarium-planetary-features/la.qm
%lang(lb) %{_datadir}/%{name}/translations/stellarium-planetary-features/lb.qm
%lang(lt) %{_datadir}/%{name}/translations/stellarium-planetary-features/lt.qm
%lang(lv) %{_datadir}/%{name}/translations/stellarium-planetary-features/lv.qm
%lang(mk) %{_datadir}/%{name}/translations/stellarium-planetary-features/mk.qm
%lang(ml) %{_datadir}/%{name}/translations/stellarium-planetary-features/ml.qm
%lang(mn) %{_datadir}/%{name}/translations/stellarium-planetary-features/mn.qm
%lang(mr) %{_datadir}/%{name}/translations/stellarium-planetary-features/mr.qm
%lang(ms) %{_datadir}/%{name}/translations/stellarium-planetary-features/ms.qm
%lang(nb) %{_datadir}/%{name}/translations/stellarium-planetary-features/nb.qm
%lang(nds) %{_datadir}/%{name}/translations/stellarium-planetary-features/nds.qm
%lang(ne) %{_datadir}/%{name}/translations/stellarium-planetary-features/ne.qm
%lang(nl) %{_datadir}/%{name}/translations/stellarium-planetary-features/nl.qm
%lang(nn) %{_datadir}/%{name}/translations/stellarium-planetary-features/nn.qm
%lang(pa) %{_datadir}/%{name}/translations/stellarium-planetary-features/pa.qm
%lang(pl) %{_datadir}/%{name}/translations/stellarium-planetary-features/pl.qm
%lang(pt) %{_datadir}/%{name}/translations/stellarium-planetary-features/pt.qm
%lang(pt_BR) %{_datadir}/%{name}/translations/stellarium-planetary-features/pt_BR.qm
%lang(ro) %{_datadir}/%{name}/translations/stellarium-planetary-features/ro.qm
%lang(ru) %{_datadir}/%{name}/translations/stellarium-planetary-features/ru.qm
%lang(sc) %{_datadir}/%{name}/translations/stellarium-planetary-features/sc.qm
%lang(si) %{_datadir}/%{name}/translations/stellarium-planetary-features/si.qm
%lang(sk) %{_datadir}/%{name}/translations/stellarium-planetary-features/sk.qm
%lang(sl) %{_datadir}/%{name}/translations/stellarium-planetary-features/sl.qm
%lang(sq) %{_datadir}/%{name}/translations/stellarium-planetary-features/sq.qm
%lang(sr) %{_datadir}/%{name}/translations/stellarium-planetary-features/sr.qm
%lang(sv) %{_datadir}/%{name}/translations/stellarium-planetary-features/sv.qm
%lang(sw) %{_datadir}/%{name}/translations/stellarium-planetary-features/sw.qm
%lang(ta) %{_datadir}/%{name}/translations/stellarium-planetary-features/ta.qm
%lang(te) %{_datadir}/%{name}/translations/stellarium-planetary-features/te.qm
%lang(tg) %{_datadir}/%{name}/translations/stellarium-planetary-features/tg.qm
%lang(th) %{_datadir}/%{name}/translations/stellarium-planetary-features/th.qm
%lang(tl) %{_datadir}/%{name}/translations/stellarium-planetary-features/tl.qm
%lang(tr) %{_datadir}/%{name}/translations/stellarium-planetary-features/tr.qm
%lang(ug) %{_datadir}/%{name}/translations/stellarium-planetary-features/ug.qm
%lang(uk) %{_datadir}/%{name}/translations/stellarium-planetary-features/uk.qm
%lang(vi) %{_datadir}/%{name}/translations/stellarium-planetary-features/vi.qm
%lang(zh) %{_datadir}/%{name}/translations/stellarium-planetary-features/zh.qm
%lang(zh_CN) %{_datadir}/%{name}/translations/stellarium-planetary-features/zh_CN.qm
%lang(zh_HK) %{_datadir}/%{name}/translations/stellarium-planetary-features/zh_HK.qm
%lang(zh_TW) %{_datadir}/%{name}/translations/stellarium-planetary-features/zh_TW.qm
%lang(af) %{_datadir}/%{name}/translations/stellarium-remotecontrol/af.qm
%lang(ar) %{_datadir}/%{name}/translations/stellarium-remotecontrol/ar.qm
%lang(ast) %{_datadir}/%{name}/translations/stellarium-remotecontrol/ast.qm
%lang(az) %{_datadir}/%{name}/translations/stellarium-remotecontrol/az.qm
%lang(be) %{_datadir}/%{name}/translations/stellarium-remotecontrol/be.qm
%lang(bg) %{_datadir}/%{name}/translations/stellarium-remotecontrol/bg.qm
%lang(bn) %{_datadir}/%{name}/translations/stellarium-remotecontrol/bn.qm
%lang(br) %{_datadir}/%{name}/translations/stellarium-remotecontrol/br.qm
%lang(bs) %{_datadir}/%{name}/translations/stellarium-remotecontrol/bs.qm
%lang(ca) %{_datadir}/%{name}/translations/stellarium-remotecontrol/ca.qm
%lang(ca@valencia) %{_datadir}/%{name}/translations/stellarium-remotecontrol/ca@valencia.qm
%lang(cs) %{_datadir}/%{name}/translations/stellarium-remotecontrol/cs.qm
%lang(cv) %{_datadir}/%{name}/translations/stellarium-remotecontrol/cv.qm
%lang(da) %{_datadir}/%{name}/translations/stellarium-remotecontrol/da.qm
%lang(de) %{_datadir}/%{name}/translations/stellarium-remotecontrol/de.qm
%lang(el) %{_datadir}/%{name}/translations/stellarium-remotecontrol/el.qm
%lang(en) %{_datadir}/%{name}/translations/stellarium-remotecontrol/en.qm
%lang(en_AU) %{_datadir}/%{name}/translations/stellarium-remotecontrol/en_AU.qm
%lang(en_CA) %{_datadir}/%{name}/translations/stellarium-remotecontrol/en_CA.qm
%lang(en_GB) %{_datadir}/%{name}/translations/stellarium-remotecontrol/en_GB.qm
%lang(en_US) %{_datadir}/%{name}/translations/stellarium-remotecontrol/en_US.qm
%lang(eo) %{_datadir}/%{name}/translations/stellarium-remotecontrol/eo.qm
%lang(es) %{_datadir}/%{name}/translations/stellarium-remotecontrol/es.qm
%lang(et) %{_datadir}/%{name}/translations/stellarium-remotecontrol/et.qm
%lang(eu) %{_datadir}/%{name}/translations/stellarium-remotecontrol/eu.qm
%lang(fa) %{_datadir}/%{name}/translations/stellarium-remotecontrol/fa.qm
%lang(fi) %{_datadir}/%{name}/translations/stellarium-remotecontrol/fi.qm
%lang(fr) %{_datadir}/%{name}/translations/stellarium-remotecontrol/fr.qm
%lang(fy) %{_datadir}/%{name}/translations/stellarium-remotecontrol/fy.qm
%lang(ga) %{_datadir}/%{name}/translations/stellarium-remotecontrol/ga.qm
%lang(gd) %{_datadir}/%{name}/translations/stellarium-remotecontrol/gd.qm
%lang(gl) %{_datadir}/%{name}/translations/stellarium-remotecontrol/gl.qm
%lang(gu) %{_datadir}/%{name}/translations/stellarium-remotecontrol/gu.qm
%lang(he) %{_datadir}/%{name}/translations/stellarium-remotecontrol/he.qm
%lang(hi) %{_datadir}/%{name}/translations/stellarium-remotecontrol/hi.qm
%lang(hr) %{_datadir}/%{name}/translations/stellarium-remotecontrol/hr.qm
%lang(hu) %{_datadir}/%{name}/translations/stellarium-remotecontrol/hu.qm
%lang(hy) %{_datadir}/%{name}/translations/stellarium-remotecontrol/hy.qm
%lang(id) %{_datadir}/%{name}/translations/stellarium-remotecontrol/id.qm
%lang(is) %{_datadir}/%{name}/translations/stellarium-remotecontrol/is.qm
%lang(it) %{_datadir}/%{name}/translations/stellarium-remotecontrol/it.qm
%lang(ja) %{_datadir}/%{name}/translations/stellarium-remotecontrol/ja.qm
%lang(jv) %{_datadir}/%{name}/translations/stellarium-remotecontrol/jv.qm
%lang(ka) %{_datadir}/%{name}/translations/stellarium-remotecontrol/ka.qm
%lang(kk) %{_datadir}/%{name}/translations/stellarium-remotecontrol/kk.qm
%lang(ko) %{_datadir}/%{name}/translations/stellarium-remotecontrol/ko.qm
%lang(ku) %{_datadir}/%{name}/translations/stellarium-remotecontrol/ku.qm
%lang(ky) %{_datadir}/%{name}/translations/stellarium-remotecontrol/ky.qm
%lang(la) %{_datadir}/%{name}/translations/stellarium-remotecontrol/la.qm
%lang(lb) %{_datadir}/%{name}/translations/stellarium-remotecontrol/lb.qm
%lang(lt) %{_datadir}/%{name}/translations/stellarium-remotecontrol/lt.qm
%lang(lv) %{_datadir}/%{name}/translations/stellarium-remotecontrol/lv.qm
%lang(mk) %{_datadir}/%{name}/translations/stellarium-remotecontrol/mk.qm
%lang(ml) %{_datadir}/%{name}/translations/stellarium-remotecontrol/ml.qm
%lang(mn) %{_datadir}/%{name}/translations/stellarium-remotecontrol/mn.qm
%lang(mr) %{_datadir}/%{name}/translations/stellarium-remotecontrol/mr.qm
%lang(ms) %{_datadir}/%{name}/translations/stellarium-remotecontrol/ms.qm
%lang(nb) %{_datadir}/%{name}/translations/stellarium-remotecontrol/nb.qm
%lang(nds) %{_datadir}/%{name}/translations/stellarium-remotecontrol/nds.qm
%lang(ne) %{_datadir}/%{name}/translations/stellarium-remotecontrol/ne.qm
%lang(nl) %{_datadir}/%{name}/translations/stellarium-remotecontrol/nl.qm
%lang(nn) %{_datadir}/%{name}/translations/stellarium-remotecontrol/nn.qm
%lang(pa) %{_datadir}/%{name}/translations/stellarium-remotecontrol/pa.qm
%lang(pl) %{_datadir}/%{name}/translations/stellarium-remotecontrol/pl.qm
%lang(pt) %{_datadir}/%{name}/translations/stellarium-remotecontrol/pt.qm
%lang(pt_BR) %{_datadir}/%{name}/translations/stellarium-remotecontrol/pt_BR.qm
%lang(ro) %{_datadir}/%{name}/translations/stellarium-remotecontrol/ro.qm
%lang(ru) %{_datadir}/%{name}/translations/stellarium-remotecontrol/ru.qm
%lang(sc) %{_datadir}/%{name}/translations/stellarium-remotecontrol/sc.qm
%lang(si) %{_datadir}/%{name}/translations/stellarium-remotecontrol/si.qm
%lang(sk) %{_datadir}/%{name}/translations/stellarium-remotecontrol/sk.qm
%lang(sl) %{_datadir}/%{name}/translations/stellarium-remotecontrol/sl.qm
%lang(sq) %{_datadir}/%{name}/translations/stellarium-remotecontrol/sq.qm
%lang(sr) %{_datadir}/%{name}/translations/stellarium-remotecontrol/sr.qm
%lang(sv) %{_datadir}/%{name}/translations/stellarium-remotecontrol/sv.qm
%lang(sw) %{_datadir}/%{name}/translations/stellarium-remotecontrol/sw.qm
%lang(ta) %{_datadir}/%{name}/translations/stellarium-remotecontrol/ta.qm
%lang(te) %{_datadir}/%{name}/translations/stellarium-remotecontrol/te.qm
%lang(tg) %{_datadir}/%{name}/translations/stellarium-remotecontrol/tg.qm
%lang(th) %{_datadir}/%{name}/translations/stellarium-remotecontrol/th.qm
%lang(tl) %{_datadir}/%{name}/translations/stellarium-remotecontrol/tl.qm
%lang(tr) %{_datadir}/%{name}/translations/stellarium-remotecontrol/tr.qm
%lang(ug) %{_datadir}/%{name}/translations/stellarium-remotecontrol/ug.qm
%lang(uk) %{_datadir}/%{name}/translations/stellarium-remotecontrol/uk.qm
%lang(vi) %{_datadir}/%{name}/translations/stellarium-remotecontrol/vi.qm
%lang(zh) %{_datadir}/%{name}/translations/stellarium-remotecontrol/zh.qm
%lang(zh_CN) %{_datadir}/%{name}/translations/stellarium-remotecontrol/zh_CN.qm
%lang(zh_HK) %{_datadir}/%{name}/translations/stellarium-remotecontrol/zh_HK.qm
%lang(zh_TW) %{_datadir}/%{name}/translations/stellarium-remotecontrol/zh_TW.qm
%lang(aa) %{_datadir}/%{name}/translations/stellarium-skycultures/aa.qm
%lang(ae) %{_datadir}/%{name}/translations/stellarium-skycultures/ae.qm
%lang(af) %{_datadir}/%{name}/translations/stellarium-skycultures/af.qm
%lang(ar) %{_datadir}/%{name}/translations/stellarium-skycultures/ar.qm
%lang(ast) %{_datadir}/%{name}/translations/stellarium-skycultures/ast.qm
%lang(av) %{_datadir}/%{name}/translations/stellarium-skycultures/av.qm
%lang(az) %{_datadir}/%{name}/translations/stellarium-skycultures/az.qm
%lang(be) %{_datadir}/%{name}/translations/stellarium-skycultures/be.qm
%lang(bg) %{_datadir}/%{name}/translations/stellarium-skycultures/bg.qm
%lang(bh) %{_datadir}/%{name}/translations/stellarium-skycultures/bh.qm
%lang(bi) %{_datadir}/%{name}/translations/stellarium-skycultures/bi.qm
%lang(bn) %{_datadir}/%{name}/translations/stellarium-skycultures/bn.qm
%lang(br) %{_datadir}/%{name}/translations/stellarium-skycultures/br.qm
%lang(bs) %{_datadir}/%{name}/translations/stellarium-skycultures/bs.qm
%lang(ca) %{_datadir}/%{name}/translations/stellarium-skycultures/ca.qm
%lang(ca@valencia) %{_datadir}/%{name}/translations/stellarium-skycultures/ca@valencia.qm
%lang(ce) %{_datadir}/%{name}/translations/stellarium-skycultures/ce.qm
%lang(cs) %{_datadir}/%{name}/translations/stellarium-skycultures/cs.qm
%lang(cv) %{_datadir}/%{name}/translations/stellarium-skycultures/cv.qm
%lang(da) %{_datadir}/%{name}/translations/stellarium-skycultures/da.qm
%lang(de) %{_datadir}/%{name}/translations/stellarium-skycultures/de.qm
%lang(el) %{_datadir}/%{name}/translations/stellarium-skycultures/el.qm
%lang(en) %{_datadir}/%{name}/translations/stellarium-skycultures/en.qm
%lang(en_AU) %{_datadir}/%{name}/translations/stellarium-skycultures/en_AU.qm
%lang(en_CA) %{_datadir}/%{name}/translations/stellarium-skycultures/en_CA.qm
%lang(en_GB) %{_datadir}/%{name}/translations/stellarium-skycultures/en_GB.qm
%lang(en_US) %{_datadir}/%{name}/translations/stellarium-skycultures/en_US.qm
%lang(eo) %{_datadir}/%{name}/translations/stellarium-skycultures/eo.qm
%lang(es) %{_datadir}/%{name}/translations/stellarium-skycultures/es.qm
%lang(et) %{_datadir}/%{name}/translations/stellarium-skycultures/et.qm
%lang(eu) %{_datadir}/%{name}/translations/stellarium-skycultures/eu.qm
%lang(fa) %{_datadir}/%{name}/translations/stellarium-skycultures/fa.qm
%lang(fi) %{_datadir}/%{name}/translations/stellarium-skycultures/fi.qm
%lang(fj) %{_datadir}/%{name}/translations/stellarium-skycultures/fj.qm
%lang(fr) %{_datadir}/%{name}/translations/stellarium-skycultures/fr.qm
%lang(fy) %{_datadir}/%{name}/translations/stellarium-skycultures/fy.qm
%lang(ga) %{_datadir}/%{name}/translations/stellarium-skycultures/ga.qm
%lang(gd) %{_datadir}/%{name}/translations/stellarium-skycultures/gd.qm
%lang(gl) %{_datadir}/%{name}/translations/stellarium-skycultures/gl.qm
%lang(gn) %{_datadir}/%{name}/translations/stellarium-skycultures/gn.qm
%lang(gu) %{_datadir}/%{name}/translations/stellarium-skycultures/gu.qm
%lang(gv) %{_datadir}/%{name}/translations/stellarium-skycultures/gv.qm
%lang(he) %{_datadir}/%{name}/translations/stellarium-skycultures/he.qm
%lang(hi) %{_datadir}/%{name}/translations/stellarium-skycultures/hi.qm
%lang(hr) %{_datadir}/%{name}/translations/stellarium-skycultures/hr.qm
%lang(hrx) %{_datadir}/%{name}/translations/stellarium-skycultures/hrx.qm
%lang(hu) %{_datadir}/%{name}/translations/stellarium-skycultures/hu.qm
%lang(hy) %{_datadir}/%{name}/translations/stellarium-skycultures/hy.qm
%lang(id) %{_datadir}/%{name}/translations/stellarium-skycultures/id.qm
%lang(is) %{_datadir}/%{name}/translations/stellarium-skycultures/is.qm
%lang(it) %{_datadir}/%{name}/translations/stellarium-skycultures/it.qm
%lang(ja) %{_datadir}/%{name}/translations/stellarium-skycultures/ja.qm
%lang(jv) %{_datadir}/%{name}/translations/stellarium-skycultures/jv.qm
%lang(ka) %{_datadir}/%{name}/translations/stellarium-skycultures/ka.qm
%lang(kg) %{_datadir}/%{name}/translations/stellarium-skycultures/kg.qm
%lang(kk) %{_datadir}/%{name}/translations/stellarium-skycultures/kk.qm
%lang(ko) %{_datadir}/%{name}/translations/stellarium-skycultures/ko.qm
%lang(ku) %{_datadir}/%{name}/translations/stellarium-skycultures/ku.qm
%lang(ky) %{_datadir}/%{name}/translations/stellarium-skycultures/ky.qm
%lang(la) %{_datadir}/%{name}/translations/stellarium-skycultures/la.qm
%lang(lb) %{_datadir}/%{name}/translations/stellarium-skycultures/lb.qm
%lang(lt) %{_datadir}/%{name}/translations/stellarium-skycultures/lt.qm
%lang(lv) %{_datadir}/%{name}/translations/stellarium-skycultures/lv.qm
%lang(mk) %{_datadir}/%{name}/translations/stellarium-skycultures/mk.qm
%lang(ml) %{_datadir}/%{name}/translations/stellarium-skycultures/ml.qm
%lang(mn) %{_datadir}/%{name}/translations/stellarium-skycultures/mn.qm
%lang(mo) %{_datadir}/%{name}/translations/stellarium-skycultures/mo.qm
%lang(moc) %{_datadir}/%{name}/translations/stellarium-skycultures/moc.qm
%lang(mr) %{_datadir}/%{name}/translations/stellarium-skycultures/mr.qm
%lang(ms) %{_datadir}/%{name}/translations/stellarium-skycultures/ms.qm
%lang(lt) %{_datadir}/%{name}/translations/stellarium/lt.qm
%lang(lv) %{_datadir}/%{name}/translations/stellarium/lv.qm
%lang(mk) %{_datadir}/%{name}/translations/stellarium/mk.qm
%lang(ml) %{_datadir}/%{name}/translations/stellarium/ml.qm
%lang(mn) %{_datadir}/%{name}/translations/stellarium/mn.qm
%lang(mo) %{_datadir}/%{name}/translations/stellarium/mo.qm
%lang(mr) %{_datadir}/%{name}/translations/stellarium/mr.qm
%lang(ms) %{_datadir}/%{name}/translations/stellarium/ms.qm
%lang(na) %{_datadir}/%{name}/translations/stellarium/na.qm
%lang(nb) %{_datadir}/%{name}/translations/stellarium/nb.qm
%lang(nds) %{_datadir}/%{name}/translations/stellarium/nds.qm
%lang(ne) %{_datadir}/%{name}/translations/stellarium/ne.qm
%lang(nl) %{_datadir}/%{name}/translations/stellarium/nl.qm
%lang(nn) %{_datadir}/%{name}/translations/stellarium/nn.qm
%lang(oj) %{_datadir}/%{name}/translations/stellarium/oj.qm
%lang(pa) %{_datadir}/%{name}/translations/stellarium/pa.qm
%lang(pl) %{_datadir}/%{name}/translations/stellarium/pl.qm
%lang(pt) %{_datadir}/%{name}/translations/stellarium/pt.qm
%lang(pt_BR) %{_datadir}/%{name}/translations/stellarium/pt_BR.qm
%lang(ro) %{_datadir}/%{name}/translations/stellarium/ro.qm
%lang(ru) %{_datadir}/%{name}/translations/stellarium/ru.qm
%lang(sc) %{_datadir}/%{name}/translations/stellarium/sc.qm
%lang(si) %{_datadir}/%{name}/translations/stellarium/si.qm
%lang(sk) %{_datadir}/%{name}/translations/stellarium/sk.qm
%lang(sl) %{_datadir}/%{name}/translations/stellarium/sl.qm
%lang(sq) %{_datadir}/%{name}/translations/stellarium/sq.qm
%lang(sr) %{_datadir}/%{name}/translations/stellarium/sr.qm
%lang(sv) %{_datadir}/%{name}/translations/stellarium/sv.qm
%lang(sw) %{_datadir}/%{name}/translations/stellarium/sw.qm
%lang(ta) %{_datadir}/%{name}/translations/stellarium/ta.qm
%lang(te) %{_datadir}/%{name}/translations/stellarium/te.qm
%lang(tg) %{_datadir}/%{name}/translations/stellarium/tg.qm
%lang(th) %{_datadir}/%{name}/translations/stellarium/th.qm
%lang(tl) %{_datadir}/%{name}/translations/stellarium/tl.qm
%lang(tr) %{_datadir}/%{name}/translations/stellarium/tr.qm
%lang(ug) %{_datadir}/%{name}/translations/stellarium/ug.qm
%lang(uk) %{_datadir}/%{name}/translations/stellarium/uk.qm
%lang(vi) %{_datadir}/%{name}/translations/stellarium/vi.qm
%lang(zh) %{_datadir}/%{name}/translations/stellarium/zh.qm
%lang(zh_CN) %{_datadir}/%{name}/translations/stellarium/zh_CN.qm
%lang(zh_HK) %{_datadir}/%{name}/translations/stellarium/zh_HK.qm
%lang(zh_TW) %{_datadir}/%{name}/translations/stellarium/zh_TW.qm
