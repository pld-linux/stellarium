%define guide_version 0.12.3-1
Summary:	Realistic sky generator
Summary(pl.UTF-8):	Realistyczny generator obrazu nieba
Name:		stellarium
Version:	0.14.1
Release:	2
License:	GPL v2+
Group:		X11/Applications/Science
Source0:	http://downloads.sourceforge.net/stellarium/%{name}-%{version}.tar.gz
# Source0-md5:	77d8f6c0087b91c2df240f2996437bfd
Source1:	http://downloads.sourceforge.net/stellarium/%{name}_user_guide-%{guide_version}.pdf
# Source1-md5:	223365806774f7f494c857bfff14df70
URL:		http://www.stellarium.org/
BuildRequires:	OpenGL-devel
BuildRequires:	Qt5Concurrent-devel
BuildRequires:	Qt5Declarative-devel
BuildRequires:	Qt5Gui-devel
BuildRequires:	Qt5Network-devel
BuildRequires:	Qt5OpenGL-devel
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
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description data
Stellarium data files

%prep
%setup -q

install %{SOURCE1} .

%build
%cmake \
		-DCMAKE_INSTALL_PREFIX=%{_prefix} \
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
%doc AUTHORS ChangeLog README %{name}_user_guide-%{guide_version}.pdf
%attr(755,root,root) %{_bindir}/*
%{_datadir}/appdata/stellarium.appdata.xml
%{_desktopdir}/%{name}.desktop
%{_mandir}/man1/%{name}.1*
%{_pixmapsdir}/%{name}.xpm
%{_iconsdir}/*/*/apps/stellarium.png

%files data
%defattr(644,root,root,755)
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/data
%{_datadir}/%{name}/landscapes
%{_datadir}/%{name}/nebulae
%{_datadir}/%{name}/scenery3d
%{_datadir}/%{name}/scripts
%{_datadir}/%{name}/skycultures
%{_datadir}/%{name}/stars
%{_datadir}/%{name}/textures
%dir %{_datadir}/%{name}/translations
%dir %{_datadir}/%{name}/translations/stellarium
%dir %{_datadir}/%{name}/translations/stellarium-skycultures
%lang(aa) %{_datadir}/%{name}/translations/stellarium-skycultures/aa.qm
%lang(ab) %{_datadir}/%{name}/translations/stellarium-skycultures/ab.qm
%lang(ae) %{_datadir}/%{name}/translations/stellarium-skycultures/ae.qm
%lang(af) %{_datadir}/%{name}/translations/stellarium-skycultures/af.qm
%lang(ak) %{_datadir}/%{name}/translations/stellarium-skycultures/ak.qm
%lang(am) %{_datadir}/%{name}/translations/stellarium-skycultures/am.qm
%lang(an) %{_datadir}/%{name}/translations/stellarium-skycultures/an.qm
%lang(ar) %{_datadir}/%{name}/translations/stellarium-skycultures/ar.qm
%lang(as) %{_datadir}/%{name}/translations/stellarium-skycultures/as.qm
%lang(ast) %{_datadir}/%{name}/translations/stellarium-skycultures/ast.qm
%lang(av) %{_datadir}/%{name}/translations/stellarium-skycultures/av.qm
%lang(az) %{_datadir}/%{name}/translations/stellarium-skycultures/az.qm
%lang(ba) %{_datadir}/%{name}/translations/stellarium-skycultures/ba.qm
%lang(be) %{_datadir}/%{name}/translations/stellarium-skycultures/be.qm
%lang(bg) %{_datadir}/%{name}/translations/stellarium-skycultures/bg.qm
%lang(bh) %{_datadir}/%{name}/translations/stellarium-skycultures/bh.qm
%lang(bi) %{_datadir}/%{name}/translations/stellarium-skycultures/bi.qm
%lang(bn) %{_datadir}/%{name}/translations/stellarium-skycultures/bn.qm
%lang(bo) %{_datadir}/%{name}/translations/stellarium-skycultures/bo.qm
%lang(br) %{_datadir}/%{name}/translations/stellarium-skycultures/br.qm
%lang(bs) %{_datadir}/%{name}/translations/stellarium-skycultures/bs.qm
%lang(ca) %{_datadir}/%{name}/translations/stellarium-skycultures/ca.qm
%lang(ce) %{_datadir}/%{name}/translations/stellarium-skycultures/ce.qm
%lang(ckb) %{_datadir}/%{name}/translations/stellarium-skycultures/ckb.qm
%lang(cs) %{_datadir}/%{name}/translations/stellarium-skycultures/cs.qm
%lang(csb) %{_datadir}/%{name}/translations/stellarium-skycultures/csb.qm
%lang(cv) %{_datadir}/%{name}/translations/stellarium-skycultures/cv.qm
%lang(cy) %{_datadir}/%{name}/translations/stellarium-skycultures/cy.qm
%lang(da) %{_datadir}/%{name}/translations/stellarium-skycultures/da.qm
%lang(de) %{_datadir}/%{name}/translations/stellarium-skycultures/de.qm
%lang(dv) %{_datadir}/%{name}/translations/stellarium-skycultures/dv.qm
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
%lang(fil) %{_datadir}/%{name}/translations/stellarium-skycultures/fil.qm
%lang(fj) %{_datadir}/%{name}/translations/stellarium-skycultures/fj.qm
%lang(fr) %{_datadir}/%{name}/translations/stellarium-skycultures/fr.qm
%lang(fy) %{_datadir}/%{name}/translations/stellarium-skycultures/fy.qm
%lang(ga) %{_datadir}/%{name}/translations/stellarium-skycultures/ga.qm
%lang(gd) %{_datadir}/%{name}/translations/stellarium-skycultures/gd.qm
%lang(gl) %{_datadir}/%{name}/translations/stellarium-skycultures/gl.qm
%lang(gn) %{_datadir}/%{name}/translations/stellarium-skycultures/gn.qm
%lang(gu) %{_datadir}/%{name}/translations/stellarium-skycultures/gu.qm
%lang(gv) %{_datadir}/%{name}/translations/stellarium-skycultures/gv.qm
%lang(haw) %{_datadir}/%{name}/translations/stellarium-skycultures/haw.qm
%lang(he) %{_datadir}/%{name}/translations/stellarium-skycultures/he.qm
%lang(hi) %{_datadir}/%{name}/translations/stellarium-skycultures/hi.qm
%lang(hne) %{_datadir}/%{name}/translations/stellarium-skycultures/hne.qm
%lang(hr) %{_datadir}/%{name}/translations/stellarium-skycultures/hr.qm
%lang(hrx) %{_datadir}/%{name}/translations/stellarium-skycultures/hrx.qm
%lang(ht) %{_datadir}/%{name}/translations/stellarium-skycultures/ht.qm
%lang(hu) %{_datadir}/%{name}/translations/stellarium-skycultures/hu.qm
%lang(hy) %{_datadir}/%{name}/translations/stellarium-skycultures/hy.qm
%lang(ia) %{_datadir}/%{name}/translations/stellarium-skycultures/ia.qm
%lang(id) %{_datadir}/%{name}/translations/stellarium-skycultures/id.qm
%lang(is) %{_datadir}/%{name}/translations/stellarium-skycultures/is.qm
%lang(it) %{_datadir}/%{name}/translations/stellarium-skycultures/it.qm
%lang(ja) %{_datadir}/%{name}/translations/stellarium-skycultures/ja.qm
%lang(jv) %{_datadir}/%{name}/translations/stellarium-skycultures/jv.qm
%lang(ka) %{_datadir}/%{name}/translations/stellarium-skycultures/ka.qm
%lang(kg) %{_datadir}/%{name}/translations/stellarium-skycultures/kg.qm
%lang(kk) %{_datadir}/%{name}/translations/stellarium-skycultures/kk.qm
%lang(km) %{_datadir}/%{name}/translations/stellarium-skycultures/km.qm
%lang(kn) %{_datadir}/%{name}/translations/stellarium-skycultures/kn.qm
%lang(ko) %{_datadir}/%{name}/translations/stellarium-skycultures/ko.qm
%lang(ky) %{_datadir}/%{name}/translations/stellarium-skycultures/ky.qm
%lang(la) %{_datadir}/%{name}/translations/stellarium-skycultures/la.qm
%lang(lb) %{_datadir}/%{name}/translations/stellarium-skycultures/lb.qm
%lang(lo) %{_datadir}/%{name}/translations/stellarium-skycultures/lo.qm
%lang(lt) %{_datadir}/%{name}/translations/stellarium-skycultures/lt.qm
%lang(lv) %{_datadir}/%{name}/translations/stellarium-skycultures/lv.qm
%lang(mai) %{_datadir}/%{name}/translations/stellarium-skycultures/mai.qm
%lang(mi) %{_datadir}/%{name}/translations/stellarium-skycultures/mi.qm
%lang(mk) %{_datadir}/%{name}/translations/stellarium-skycultures/mk.qm
%lang(ml) %{_datadir}/%{name}/translations/stellarium-skycultures/ml.qm
%lang(mn) %{_datadir}/%{name}/translations/stellarium-skycultures/mn.qm
%lang(mo) %{_datadir}/%{name}/translations/stellarium-skycultures/mo.qm
%lang(mr) %{_datadir}/%{name}/translations/stellarium-skycultures/mr.qm
%lang(ms) %{_datadir}/%{name}/translations/stellarium-skycultures/ms.qm
%lang(mt) %{_datadir}/%{name}/translations/stellarium-skycultures/mt.qm
%lang(na) %{_datadir}/%{name}/translations/stellarium-skycultures/na.qm
%lang(nan) %{_datadir}/%{name}/translations/stellarium-skycultures/nan.qm
%lang(nb) %{_datadir}/%{name}/translations/stellarium-skycultures/nb.qm
%lang(nds) %{_datadir}/%{name}/translations/stellarium-skycultures/nds.qm
%lang(ne) %{_datadir}/%{name}/translations/stellarium-skycultures/ne.qm
%lang(nl) %{_datadir}/%{name}/translations/stellarium-skycultures/nl.qm
%lang(nn) %{_datadir}/%{name}/translations/stellarium-skycultures/nn.qm
%lang(oc) %{_datadir}/%{name}/translations/stellarium-skycultures/oc.qm
%lang(os) %{_datadir}/%{name}/translations/stellarium-skycultures/os.qm
%lang(pa) %{_datadir}/%{name}/translations/stellarium-skycultures/pa.qm
%lang(pl) %{_datadir}/%{name}/translations/stellarium-skycultures/pl.qm
%lang(pt) %{_datadir}/%{name}/translations/stellarium-skycultures/pt.qm
%lang(pt_BR) %{_datadir}/%{name}/translations/stellarium-skycultures/pt_BR.qm
%lang(ro) %{_datadir}/%{name}/translations/stellarium-skycultures/ro.qm
%lang(ru) %{_datadir}/%{name}/translations/stellarium-skycultures/ru.qm
%lang(sah) %{_datadir}/%{name}/translations/stellarium-skycultures/sah.qm
%lang(sco) %{_datadir}/%{name}/translations/stellarium-skycultures/sco.qm
%lang(se) %{_datadir}/%{name}/translations/stellarium-skycultures/se.qm
%lang(si) %{_datadir}/%{name}/translations/stellarium-skycultures/si.qm
%lang(sk) %{_datadir}/%{name}/translations/stellarium-skycultures/sk.qm
%lang(sl) %{_datadir}/%{name}/translations/stellarium-skycultures/sl.qm
%lang(sm) %{_datadir}/%{name}/translations/stellarium-skycultures/sm.qm
%lang(sq) %{_datadir}/%{name}/translations/stellarium-skycultures/sq.qm
%lang(sr) %{_datadir}/%{name}/translations/stellarium-skycultures/sr.qm
%lang(su) %{_datadir}/%{name}/translations/stellarium-skycultures/su.qm
%lang(sv) %{_datadir}/%{name}/translations/stellarium-skycultures/sv.qm
%lang(sw) %{_datadir}/%{name}/translations/stellarium-skycultures/sw.qm
%lang(ta) %{_datadir}/%{name}/translations/stellarium-skycultures/ta.qm
%lang(te) %{_datadir}/%{name}/translations/stellarium-skycultures/te.qm
%lang(tg) %{_datadir}/%{name}/translations/stellarium-skycultures/tg.qm
%lang(th) %{_datadir}/%{name}/translations/stellarium-skycultures/th.qm
%lang(tl) %{_datadir}/%{name}/translations/stellarium-skycultures/tl.qm
%lang(tr) %{_datadir}/%{name}/translations/stellarium-skycultures/tr.qm
%lang(tt) %{_datadir}/%{name}/translations/stellarium-skycultures/tt.qm
%lang(ug) %{_datadir}/%{name}/translations/stellarium-skycultures/ug.qm
%lang(uk) %{_datadir}/%{name}/translations/stellarium-skycultures/uk.qm
%lang(uz) %{_datadir}/%{name}/translations/stellarium-skycultures/uz.qm
%lang(vi) %{_datadir}/%{name}/translations/stellarium-skycultures/vi.qm
%lang(wa) %{_datadir}/%{name}/translations/stellarium-skycultures/wa.qm
%lang(xh) %{_datadir}/%{name}/translations/stellarium-skycultures/xh.qm
%lang(zh_CN) %{_datadir}/%{name}/translations/stellarium-skycultures/zh_CN.qm
%lang(zh_HK) %{_datadir}/%{name}/translations/stellarium-skycultures/zh_HK.qm
%lang(zh_TW) %{_datadir}/%{name}/translations/stellarium-skycultures/zh_TW.qm
%lang(zu) %{_datadir}/%{name}/translations/stellarium-skycultures/zu.qm
%lang(aa) %{_datadir}/%{name}/translations/stellarium/aa.qm
%lang(ab) %{_datadir}/%{name}/translations/stellarium/ab.qm
%lang(ae) %{_datadir}/%{name}/translations/stellarium/ae.qm
%lang(af) %{_datadir}/%{name}/translations/stellarium/af.qm
%lang(ak) %{_datadir}/%{name}/translations/stellarium/ak.qm
%lang(am) %{_datadir}/%{name}/translations/stellarium/am.qm
%lang(an) %{_datadir}/%{name}/translations/stellarium/an.qm
%lang(ar) %{_datadir}/%{name}/translations/stellarium/ar.qm
%lang(as) %{_datadir}/%{name}/translations/stellarium/as.qm
%lang(ast) %{_datadir}/%{name}/translations/stellarium/ast.qm
%lang(av) %{_datadir}/%{name}/translations/stellarium/av.qm
%lang(az) %{_datadir}/%{name}/translations/stellarium/az.qm
%lang(ba) %{_datadir}/%{name}/translations/stellarium/ba.qm
%lang(be) %{_datadir}/%{name}/translations/stellarium/be.qm
%lang(bg) %{_datadir}/%{name}/translations/stellarium/bg.qm
%lang(bh) %{_datadir}/%{name}/translations/stellarium/bh.qm
%lang(bi) %{_datadir}/%{name}/translations/stellarium/bi.qm
%lang(bn) %{_datadir}/%{name}/translations/stellarium/bn.qm
%lang(bo) %{_datadir}/%{name}/translations/stellarium/bo.qm
%lang(br) %{_datadir}/%{name}/translations/stellarium/br.qm
%lang(bs) %{_datadir}/%{name}/translations/stellarium/bs.qm
%lang(ca) %{_datadir}/%{name}/translations/stellarium/ca.qm
%lang(ce) %{_datadir}/%{name}/translations/stellarium/ce.qm
%lang(ckb) %{_datadir}/%{name}/translations/stellarium/ckb.qm
%lang(cs) %{_datadir}/%{name}/translations/stellarium/cs.qm
%lang(csb) %{_datadir}/%{name}/translations/stellarium/csb.qm
%lang(cv) %{_datadir}/%{name}/translations/stellarium/cv.qm
%lang(cy) %{_datadir}/%{name}/translations/stellarium/cy.qm
%lang(da) %{_datadir}/%{name}/translations/stellarium/da.qm
%lang(de) %{_datadir}/%{name}/translations/stellarium/de.qm
%lang(dv) %{_datadir}/%{name}/translations/stellarium/dv.qm
%lang(el) %{_datadir}/%{name}/translations/stellarium/el.qm
%lang(en) %{_datadir}/%{name}/translations/stellarium/en.qm
%lang(en_AU) %{_datadir}/%{name}/translations/stellarium/en_AU.qm
%lang(en_CA) %{_datadir}/%{name}/translations/stellarium/en_CA.qm
%lang(en_GB) %{_datadir}/%{name}/translations/stellarium/en_GB.qm
%lang(en_US) %{_datadir}/%{name}/translations/stellarium/en_US.qm
%lang(eo) %{_datadir}/%{name}/translations/stellarium/eo.qm
%lang(es) %{_datadir}/%{name}/translations/stellarium/es.qm
%lang(et) %{_datadir}/%{name}/translations/stellarium/et.qm
%lang(eu) %{_datadir}/%{name}/translations/stellarium/eu.qm
%lang(fa) %{_datadir}/%{name}/translations/stellarium/fa.qm
%lang(fi) %{_datadir}/%{name}/translations/stellarium/fi.qm
%lang(fil) %{_datadir}/%{name}/translations/stellarium/fil.qm
%lang(fj) %{_datadir}/%{name}/translations/stellarium/fj.qm
%lang(fr) %{_datadir}/%{name}/translations/stellarium/fr.qm
%lang(fy) %{_datadir}/%{name}/translations/stellarium/fy.qm
%lang(ga) %{_datadir}/%{name}/translations/stellarium/ga.qm
%lang(gd) %{_datadir}/%{name}/translations/stellarium/gd.qm
%lang(gl) %{_datadir}/%{name}/translations/stellarium/gl.qm
%lang(gn) %{_datadir}/%{name}/translations/stellarium/gn.qm
%lang(gu) %{_datadir}/%{name}/translations/stellarium/gu.qm
%lang(gv) %{_datadir}/%{name}/translations/stellarium/gv.qm
%lang(haw) %{_datadir}/%{name}/translations/stellarium/haw.qm
%lang(he) %{_datadir}/%{name}/translations/stellarium/he.qm
%lang(hi) %{_datadir}/%{name}/translations/stellarium/hi.qm
%lang(hne) %{_datadir}/%{name}/translations/stellarium/hne.qm
%lang(hr) %{_datadir}/%{name}/translations/stellarium/hr.qm
%lang(hrx) %{_datadir}/%{name}/translations/stellarium/hrx.qm
%lang(ht) %{_datadir}/%{name}/translations/stellarium/ht.qm
%lang(hu) %{_datadir}/%{name}/translations/stellarium/hu.qm
%lang(hy) %{_datadir}/%{name}/translations/stellarium/hy.qm
%lang(ia) %{_datadir}/%{name}/translations/stellarium/ia.qm
%lang(id) %{_datadir}/%{name}/translations/stellarium/id.qm
%lang(is) %{_datadir}/%{name}/translations/stellarium/is.qm
%lang(it) %{_datadir}/%{name}/translations/stellarium/it.qm
%lang(ja) %{_datadir}/%{name}/translations/stellarium/ja.qm
%lang(jv) %{_datadir}/%{name}/translations/stellarium/jv.qm
%lang(ka) %{_datadir}/%{name}/translations/stellarium/ka.qm
%lang(kg) %{_datadir}/%{name}/translations/stellarium/kg.qm
%lang(kk) %{_datadir}/%{name}/translations/stellarium/kk.qm
%lang(km) %{_datadir}/%{name}/translations/stellarium/km.qm
%lang(kn) %{_datadir}/%{name}/translations/stellarium/kn.qm
%lang(ko) %{_datadir}/%{name}/translations/stellarium/ko.qm
%lang(ky) %{_datadir}/%{name}/translations/stellarium/ky.qm
%lang(la) %{_datadir}/%{name}/translations/stellarium/la.qm
%lang(lb) %{_datadir}/%{name}/translations/stellarium/lb.qm
%lang(lo) %{_datadir}/%{name}/translations/stellarium/lo.qm
%lang(lt) %{_datadir}/%{name}/translations/stellarium/lt.qm
%lang(lv) %{_datadir}/%{name}/translations/stellarium/lv.qm
%lang(mai) %{_datadir}/%{name}/translations/stellarium/mai.qm
%lang(mi) %{_datadir}/%{name}/translations/stellarium/mi.qm
%lang(mk) %{_datadir}/%{name}/translations/stellarium/mk.qm
%lang(ml) %{_datadir}/%{name}/translations/stellarium/ml.qm
%lang(mn) %{_datadir}/%{name}/translations/stellarium/mn.qm
%lang(mo) %{_datadir}/%{name}/translations/stellarium/mo.qm
%lang(mr) %{_datadir}/%{name}/translations/stellarium/mr.qm
%lang(ms) %{_datadir}/%{name}/translations/stellarium/ms.qm
%lang(mt) %{_datadir}/%{name}/translations/stellarium/mt.qm
%lang(na) %{_datadir}/%{name}/translations/stellarium/na.qm
%lang(nan) %{_datadir}/%{name}/translations/stellarium/nan.qm
%lang(nb) %{_datadir}/%{name}/translations/stellarium/nb.qm
%lang(nds) %{_datadir}/%{name}/translations/stellarium/nds.qm
%lang(ne) %{_datadir}/%{name}/translations/stellarium/ne.qm
%lang(nl) %{_datadir}/%{name}/translations/stellarium/nl.qm
%lang(nn) %{_datadir}/%{name}/translations/stellarium/nn.qm
%lang(oc) %{_datadir}/%{name}/translations/stellarium/oc.qm
%lang(os) %{_datadir}/%{name}/translations/stellarium/os.qm
%lang(pa) %{_datadir}/%{name}/translations/stellarium/pa.qm
%lang(pl) %{_datadir}/%{name}/translations/stellarium/pl.qm
%lang(pt) %{_datadir}/%{name}/translations/stellarium/pt.qm
%lang(pt_BR) %{_datadir}/%{name}/translations/stellarium/pt_BR.qm
%lang(ro) %{_datadir}/%{name}/translations/stellarium/ro.qm
%lang(ru) %{_datadir}/%{name}/translations/stellarium/ru.qm
%lang(sah) %{_datadir}/%{name}/translations/stellarium/sah.qm
%lang(sco) %{_datadir}/%{name}/translations/stellarium/sco.qm
%lang(se) %{_datadir}/%{name}/translations/stellarium/se.qm
%lang(si) %{_datadir}/%{name}/translations/stellarium/si.qm
%lang(sk) %{_datadir}/%{name}/translations/stellarium/sk.qm
%lang(sl) %{_datadir}/%{name}/translations/stellarium/sl.qm
%lang(sm) %{_datadir}/%{name}/translations/stellarium/sm.qm
%lang(sq) %{_datadir}/%{name}/translations/stellarium/sq.qm
%lang(sr) %{_datadir}/%{name}/translations/stellarium/sr.qm
%lang(su) %{_datadir}/%{name}/translations/stellarium/su.qm
%lang(sv) %{_datadir}/%{name}/translations/stellarium/sv.qm
%lang(sw) %{_datadir}/%{name}/translations/stellarium/sw.qm
%lang(ta) %{_datadir}/%{name}/translations/stellarium/ta.qm
%lang(te) %{_datadir}/%{name}/translations/stellarium/te.qm
%lang(tg) %{_datadir}/%{name}/translations/stellarium/tg.qm
%lang(th) %{_datadir}/%{name}/translations/stellarium/th.qm
%lang(tl) %{_datadir}/%{name}/translations/stellarium/tl.qm
%lang(tr) %{_datadir}/%{name}/translations/stellarium/tr.qm
%lang(tt) %{_datadir}/%{name}/translations/stellarium/tt.qm
%lang(ug) %{_datadir}/%{name}/translations/stellarium/ug.qm
%lang(uk) %{_datadir}/%{name}/translations/stellarium/uk.qm
%lang(uz) %{_datadir}/%{name}/translations/stellarium/uz.qm
%lang(vi) %{_datadir}/%{name}/translations/stellarium/vi.qm
%lang(wa) %{_datadir}/%{name}/translations/stellarium/wa.qm
%lang(xh) %{_datadir}/%{name}/translations/stellarium/xh.qm
%lang(zh_CN) %{_datadir}/%{name}/translations/stellarium/zh_CN.qm
%lang(zh_HK) %{_datadir}/%{name}/translations/stellarium/zh_HK.qm
%lang(zh_TW) %{_datadir}/%{name}/translations/stellarium/zh_TW.qm
%lang(zu) %{_datadir}/%{name}/translations/stellarium/zu.qm
