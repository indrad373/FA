import streamlit as st

st.set_page_config(page_title="Pertanyaan", page_icon="👈")

###################################################################################33

st.title('Pertanyaan seputar persona anak')
st.text('Disini anda diminta untuk menjawab pertanyaan secara teliti dan jujur.\nSilahkan menjawab 👋👇')
st.divider()

st.markdown(
    """ <style>
            div[role="radiogroup"] >  :first-child{
                display: none !important;
            }
        </style>
        """,
    unsafe_allow_html=True
)

visual = 0
auditory = 0
readwrite = 0
kinesthetic = 0
        

question_1 = st.radio('Bagaimana anak Anda belajar tentang kebutuhan menjaga kesehatan yang baik?',
    ('',
     'Berpartisipasi aktif dalam rutinitas kebersihan atau berpartisipasi dalam aktivitas fisik terkait kesehatan.',
     'Diskusi tentang nutrisi dan kebiasaan makan sehat.',
     'Membaca tentang kesehatan mental dan kesejahteraan emosional atau menulis tentang kebersihan diri.',
     'Melalui diagram dan grafik yang menunjukkan pentingnya perawatan medis dan kesehatan fisik.'
     )
)

if question_1 == 'Berpartisipasi aktif dalam rutinitas kebersihan atau berpartisipasi dalam aktivitas fisik terkait kesehatan.':
    question_1 = 'K'
    kinesthetic = kinesthetic + 1
elif question_1 == 'Diskusi tentang nutrisi dan kebiasaan makan sehat.':
    question_1 = 'A'
    auditory = auditory + 1
elif question_1 == 'Membaca tentang kesehatan mental dan kesejahteraan emosional atau menulis tentang kebersihan diri.':
    question_1 = 'R/W'
    readwrite = readwrite + 1
elif question_1 == 'Melalui diagram dan grafik yang menunjukkan pentingnya perawatan medis dan kesehatan fisik.':
    question_1 = 'V'
    visual = visual + 1
else:
    visual = 0
    auditory = 0
    readwrite = 0
    kinesthetic = 0

st.divider()

question_2 = st.radio('Bagaimana anak Anda lebih suka memperoleh pengetahuan dan terlibat dalam aktivitas pendidikan?',
    ('',
     'Melalui presentasi atau video pendidikan di lingkungan sekolah formal.',
     'Melalui rekaman audio dan memanfaatkan sumber belajar online.',
     'Membuat catatan selama sesi dukungan akademik.',
     'Melakukan aktivitas pembelajaran interaktif yang melibatkan gerakan.'
     )
)

if question_2 == 'Melalui presentasi atau video pendidikan di lingkungan sekolah formal.':
    question_2 = 'V'
    visual = visual + 1
elif question_2 == 'Melalui rekaman audio dan memanfaatkan sumber belajar online.':
    question_2 = 'A'
    auditory = auditory + 1
elif question_2 == 'Membuat catatan selama sesi dukungan akademik.':
    question_2 = 'R/W'
    readwrite = readwrite + 1
elif question_2 == 'Melakukan aktivitas pembelajaran interaktif yang melibatkan gerakan.':
    question_2 = 'K'
    kinesthetic = kinesthetic + 1
else:
    visual = 0
    auditory = 0
    readwrite = 0
    kinesthetic = 0

st.divider()

question_3 = st.radio('Bagaimana anak Anda membutuhkan interaksi dan terlibat dengan teman sebaya?',
    ('',
     'Berpartisipasi dalam aktivitas fisik atau proyek kelompok dengan teman sebaya.',
     'Berpartisipasi dalam kegiatan kelompok, mengamati interaksi sosial dan kegiatan kelompok.',
     'Mendukung dalam membangun hubungan sosial yang sehat dengan mendengarkan percakapan dan komunikasi verbal dengan rekan sebaya.',
     'Bertukar pesan atau komunikasi tertulis dalam sebuah kelompok.'
     )
)

if question_3 == 'Berpartisipasi dalam aktivitas fisik atau proyek kelompok dengan teman sebaya.':
    question_3 = 'K'
    kinesthetic = kinesthetic + 1
elif question_3 == 'Berpartisipasi dalam kegiatan kelompok, mengamati interaksi sosial dan kegiatan kelompok.':
    question_3 = 'V'
    visual = visual + 1
elif question_3 == 'Bertukar pesan atau komunikasi tertulis dalam sebuah kelompok.':
    question_3 = 'R/W'
    readwrite = readwrite + 1
elif question_3 == 'Mendukung dalam membangun hubungan sosial yang sehat dengan mendengarkan percakapan dan komunikasi verbal dengan rekan sebaya.':
    question_3 = 'A'
    auditory = auditory + 1
else:
    visual = 0
    auditory = 0
    readwrite = 0
    kinesthetic = 0

st.divider()

question_4 = st.radio('Bagaimana anak Anda lebih suka terlibat dalam kegiatan ekstrakurikuler?',
    ('',
     'Berpartisipasi secara aktif dan terlibat secara fisik dalam aktivitas praktis yang terkait dengan minat mereka.',
     'Mencari instruksi untuk terlibat sambil berpartisipasi dalam kegiatan ekstrakurikuler.',
     'Menonton dan meniru gerakan fisik dalam olahraga atau aktivitas artistik.',
     'Membuat catatan tentang aturan dan pedoman klub atau organisasi siswa.'
     )
)

if question_4 == 'Berpartisipasi secara aktif dan terlibat secara fisik dalam aktivitas praktis yang terkait dengan minat mereka.':
    question_4 = 'K'
    kinesthetic = kinesthetic + 1
elif question_4 == 'Mencari dan mendengar instruksi untuk terlibat sambil berpartisipasi dalam kegiatan ekstrakurikuler.':
    question_4 = 'A'
    auditory = auditory + 1
elif question_4 == 'Menonton dan meniru gerakan fisik dalam olahraga atau aktivitas artistik.':
    question_4 = 'V'
    visual = visual + 1
elif question_4 == 'Membuat catatan tentang aturan dan pedoman klub atau organisasi siswa.':
    question_4 = 'R/W'
    readwrite = readwrite + 1
else:
    visual = 0
    auditory = 0
    readwrite = 0
    kinesthetic = 0

st.divider()

question_5 = st.radio('Bagaimana anak Anda menerima dukungan emosional dan meningkatkan kehatan mental?',
    ('',
     'Melalui meditasi dan musik terpandu untuk mengurangi stres.',
     'Melalui gambar yang mewakili berbagai emosi dan strategi penanganan.',
     'Melalui latihan kesadaran untuk mengelola emosi dan kesehatan mental.',
     'Melalui jurnal atau membaca buku-buku self-help terkait pengelolaan emosional.'
     )
)

if question_5 == 'Melalui meditasi terpandu untuk mengurangi stres.':
    question_5 = 'A'
    auditory = auditory + 1
elif question_5 == 'Melalui gambar yang mewakili berbagai emosi dan strategi penanganan.':
    question_5 = 'V'
    visual = visual + 1
elif question_5 == 'Melalui latihan kesadaran untuk mengelola emosi dan kesehatan mental.':
    question_5 = 'K'
    kinesthetic = kinesthetic + 1
elif question_5 == 'Melalui jurnal atau membaca buku-buku self-help terkait kesejahteraan emosional.':
    question_5 = 'R/W'
    readwrite = readwrite + 1
else:
    visual = 0
    auditory = 0
    readwrite = 0
    kinesthetic = 0

st.divider()

question_6 = st.radio('Bagaimana anak Anda lebih suka terlibat dan belajar dalam area akademik terbaik mereka?',
    ('',
     'Terlibat dalam proyek seni yang praktis atau latihan kreatif untuk meningkatkan keterampilan mereka.',
     'Membaca artikel ilmiah atau menulis makalah penelitian di bidang yang mereka kuasai.',
     'Melalui representasi visual dalam matematika atau subjek terkait logis.',
     'Terlibat dalam diskusi terkait dan menulis catatan pada subjek terkait.'
     )
)

if question_6 == 'Melalui representasi visual dalam matematika atau subjek terkait logis.':
    question_6 = 'V'
    visual = visual + 1
elif question_6 == 'Terlibat dalam diskusi terkait dan menulis catatan pada subjek terkait.':
    question_6 = 'A'
    auditory = auditory + 1
elif question_6 == 'Membaca artikel ilmiah atau menulis makalah penelitian di bidang yang mereka kuasai.':
    question_6 = 'R/W'
    readwrite = readwrite + 1
elif question_6 == 'Terlibat dalam proyek seni yang praktis atau latihan kreatif untuk meningkatkan keterampilan mereka.':
    question_6 = 'K'
    kinesthetic = kinesthetic + 1
else:
    visual = 0
    auditory = 0
    readwrite = 0
    kinesthetic = 0

st.divider()

question_7 = st.radio('Bagaimana anak Anda lebih suka untuk mengembangkan dan menampilkan keterampilan praktis atau kreatif mereka?',
    ('',
     'Eksperimen dengan teknologi atau terlibat dalam latihan pemrograman untuk mengembangkan keterampilan teknologi mereka.',
     'Mendengarkan musik atau irama untuk meningkatkan kemampuan tari atau gerakan fisik.',
     'Mengamati dan meniru nada musik atau teknik artistik.',
     'Terlibat dalam menulis kreatif untuk memupuk keterampilan artistik mereka.'
     )
)

if question_7 == 'Mengamati dan meniru nada musik atau teknik artistik.':
    question_7 = 'V'
    visual = visual + 1
elif question_7 == 'Mendengarkan musik atau irama untuk meningkatkan kemampuan tari atau gerakan fisik.':
    question_7 = 'A'
    auditory = auditory + 1
elif question_7 == 'Terlibat dalam menulis kreatif untuk memupuk keterampilan artistik mereka.':
    question_7 = 'R/W'
    readwrite = readwrite + 1
elif question_7 == 'Eksperimen dengan teknologi atau terlibat dalam latihan pemrograman untuk mengembangkan keterampilan teknologi mereka.':
    question_7 = 'K'
    kinesthetic = kinesthetic + 1
else:
    visual = 0
    auditory = 0
    readwrite = 0
    kinesthetic = 0

st.divider()

question_8 = st.radio('Bagaimana anak Anda lebih suka mengembangkan dan menampilkan keterampilan fisik atau olahraga mereka?',
    ('',
     'Membaca tentang teknik olahraga yang berbeda atau berlatih keterampilan motorik halus melalui latihan menulis.',
     'Berpartisipasi dalam aktivitas fisik atau terlibat dalam latihan keseimbangan dan koordinasi.',
     'Mendengarkan instruksi atau umpan balik dari pelatih saat terlibat dalam aktivitas olahraga.',
     'Mengamati dan meniru teknik olahraga atau gerakan tubuh.'
     )
)

if question_8 == 'Mengamati dan meniru teknik olahraga atau gerakan tubuh.':
    question_8 = 'V'
    visual = visual + 1
elif question_8 == 'Mendengarkan instruksi atau umpan balik dari pelatih saat terlibat dalam aktivitas olahraga.':
    question_8 = 'A'
    auditory = auditory + 1
elif question_8 == 'Membaca tentang teknik olahraga yang berbeda atau berlatih keterampilan motorik halus melalui latihan menulis.':
    question_8 = 'R/W'
    readwrite = readwrite + 1
elif question_8 == 'Berpartisipasi dalam aktivitas fisik atau terlibat dalam latihan keseimbangan dan koordinasi.':
    question_8 = 'K'
    kinesthetic = kinesthetic + 1
else:
    visual = 0
    auditory = 0
    readwrite = 0
    kinesthetic = 0

st.divider()

question_9 = st.radio('Bagaimana anak Anda lebih suka mengembangkan bakat atau minat khusus mereka?',
    ('',
     'Melakukan penelitian dan membaca artikel ilmiah di bidang minat mereka.',
     'Mendengarkan instruksi atau skrip dalam drama atau pertunjukan panggung.',
     'Mengambil peran kepemimpinan atau berpartisipasi aktif dalam aktivitas organisasi yang terkait dengan bakat atau minat mereka.',
     'Meniru teknik seni visual atau melalui gambar.'
     )
)

if question_9 == 'Meniru teknik seni visual atau melalui gambar.':
    question_9 = 'V'
    visual = visual + 1
elif question_9 == 'Mendengarkan instruksi atau skrip dalam drama atau pertunjukan panggung.':
    question_9 = 'A'
    auditory = auditory + 1
elif question_9 == 'Melakukan penelitian dan membaca artikel ilmiah di bidang minat mereka.':
    question_9 = 'R/W'
    readwrite = readwrite + 1
elif question_9 == 'Mengambil peran kepemimpinan atau berpartisipasi aktif dalam aktivitas organisasi yang terkait dengan bakat atau minat mereka.':
    question_9 = 'K'
    kinesthetic = kinesthetic + 1
else:
    visual = 0
    auditory = 0
    readwrite = 0
    kinesthetic = 0

st.divider()

question_10 = st.radio('Bagaimana anak Anda lebih suka meningkatkan kemampuan komunikasi dan interaksi mereka?',
    ('',
     'Berlatih berbicara di depan umum atau terlibat dalam aktivitas peran untuk mengembangkan keterampilan berbicara di depan umum.',
     'Menggunakan gerakan visual untuk mendukung komunikasi verbal mereka.',
     'Membaca buku tentang keterampilan sosial atau menulis refleksi untuk meningkatkan kemampuan komunikasi mereka.',
     'Mendengarkan dengan saksama orang lain dan terlibat dalam percakapan untuk memahami perspektif yang berbeda.'
     )
)

if question_10 == 'Menggunakan gerakan visual untuk mendukung komunikasi verbal mereka.':
    question_10 = 'V'
    visual = visual + 1
elif question_10 == 'Mendengarkan dengan saksama orang lain dan terlibat dalam percakapan untuk memahami perspektif yang berbeda.':
    question_10 = 'A'
    auditory = auditory + 1
elif question_10 == 'Membaca buku tentang keterampilan sosial atau menulis refleksi untuk meningkatkan kemampuan komunikasi mereka.':
    question_10 = 'R/W'
    readwrite = readwrite + 1
elif question_10 == 'Berlatih berbicara di depan umum atau terlibat dalam aktivitas peran untuk mengembangkan keterampilan berbicara di depan umum.':
    question_10 = 'K'
    kinesthetic = kinesthetic + 1
else:
    visual = 0
    auditory = 0
    readwrite = 0
    kinesthetic = 0

st.divider()

question_11 = st.radio('Bagaimana anak Anda lebih suka belajar dan berkembang melalui pengalaman sosial?',
    ('',
     'Melalui menghadiri acara budaya atau seni dan mengamati dinamika sosial dan interaksi.',
     'Melalui membaca dan meneliti tentang berbagai klub atau kelompok untuk membuat keputusan yang tepat tentang keterlibatan.',
     'Melalui partisipasi aktif dan interaksi dengan rekan sebaya selama kegiatan kelompok.',
     'Melalui pengalaman langsung dan terlibat secara aktif dalam kegiatan sukarela atau proyek layanan masyarakat.'
     )
)

if question_11 == 'Melalui menghadiri acara budaya atau seni dan mengamati dinamika sosial dan interaksi.':
    question_11 = 'V'
    visual = visual + 1
elif question_11 == 'Melalui partisipasi aktif dan interaksi dengan rekan sebaya selama kegiatan kelompok.':
    question_11 = 'A'
    auditory = auditory + 1
elif question_11 == 'Melalui membaca dan meneliti tentang berbagai klub atau kelompok untuk membuat keputusan yang tepat tentang keterlibatan.':
    question_11 = 'R/W'
    readwrite = readwrite + 1
elif question_11 == 'Melalui pengalaman langsung dan terlibat secara aktif dalam kegiatan sukarela atau proyek layanan masyarakat.':
    question_11 = 'K'
    kinesthetic = kinesthetic + 1
else:
    visual = 0
    auditory = 0
    readwrite = 0
    kinesthetic = 0

st.divider()

question_12 = st.radio('Bagaimana anak Anda lebih suka belajar dan mendapatkan manfaat dari bepergian dan menjelajahi lingkungan baru?',
    ('',
     'Mendengarkan cerita lokal dan percakapan untuk belajar tentang budaya yang berbeda.',
     'Membaca dan melakukan penelitian tentang sejarah dan signifikansi tempat yang dikunjungi.',
     'Mengamati dan menyerap lingkungan saat bepergian.',
     'Melalui pengalaman seperti terlibat secara aktif dalam aktivitas luar ruangan dan eksplorasi praktis.'
     )
)

if question_12 == 'Mengamati dan menyerap lingkungan saat bepergian.':
    question_12 = 'V'
    visual = visual + 1
elif question_12 == 'Mendengarkan cerita lokal dan percakapan untuk belajar tentang budaya yang berbeda.':
    question_12 = 'A'
    auditory = auditory + 1
elif question_12 == 'Membaca dan melakukan penelitian tentang sejarah dan signifikansi tempat yang dikunjungi.':
    question_12 = 'R/W'
    readwrite = readwrite + 1
elif question_12 == 'Melalui pengalaman seperti terlibat secara aktif dalam aktivitas luar ruangan dan eksplorasi praktis.':
    question_12 = 'K'
    kinesthetic = kinesthetic + 1
else:
    visual = 0
    auditory = 0
    readwrite = 0
    kinesthetic = 0

st.divider()

question_13 = st.radio('Bagaimana anak Anda lebih suka terlibat dengan teknologi digital dan internet untuk tujuan belajar?',
    ('',
     'Menerapkan keterampilan digital melalui proyek atau simulasi interaktif.',
     'Mendengarkan sekolah atau pelajaran online atau terlibat dalam diskusi virtual.',
     'Membaca buku online atau berkolaborasi melalui platform media sosial.',
     'Menggunakan perangkat lunak pendidikan interaktif atau menonton video instruksional.'
     )
)

if question_13 == 'Menggunakan perangkat lunak pendidikan interaktif atau menonton video instruksional.':
    question_13 = 'V'
    visual = visual + 1
elif question_13 == 'Mendengarkan sekolah atau pelajaran online atau terlibat dalam diskusi virtual.':
    question_13 = 'A'
    auditory = auditory + 1
elif question_13 == 'Membaca buku online atau berkolaborasi melalui platform media sosial.':
    question_13 = 'R/W'
    readwrite = readwrite + 1
elif question_13 == 'Menerapkan keterampilan digital melalui proyek atau simulasi interaktif.':
    question_13 = 'K'
    kinesthetic = kinesthetic + 1
else:
    visual = 0
    auditory = 0
    readwrite = 0
    kinesthetic = 0

st.divider()

question_14 = st.radio('Bagaimana anak Anda lebih suka terlibat dalam kegiatan sukarela atau ikut membantu dalam pelayanan masyarakat dilingkungan sekolah atau rumah untuk belajar sesuatu yang baru?',
    ('',
     'Berpartisipasi dalam aktivitas praktis dan menerapkan keterampilan dalam konteks kehidupan nyata.',
     'Membuat catatan tentang dampak kegiatan sukarela atau proyek layanan masyarakat.',
     'Mendapatkan dan mendengar arahan dari penyelenggara atau mentor.',
     'Belajar dari orang lain selama kegiatan sukarela.'
     )
)

if question_14 == 'Belajar dari orang lain selama kegiatan sukarela.':
    question_14 = 'V'
    visual = visual + 1
elif question_14 == 'Mendapatkan dan mendengar arahan dari penyelenggara atau mentor.':
    question_14 = 'A'
    auditory = auditory + 1
elif question_14 == 'Membuat catatan tentang dampak kegiatan sukarela atau proyek layanan masyarakat.':
    question_14 = 'R/W'
    readwrite = readwrite + 1
elif question_14 == 'Berpartisipasi dalam aktivitas praktis dan menerapkan keterampilan dalam konteks kehidupan nyata.':
    question_14 = 'K'
    kinesthetic = kinesthetic + 1
else:
    visual = 0
    auditory = 0
    readwrite = 0
    kinesthetic = 0

st.divider()

question_15 = st.radio('Bagaimana anak Anda lebih suka belajar dan menemukan makna dalam pengalaman yang berkesan?',
    ('',
     'Berdiskusi atau berbagi pengalaman berkesan melalui obrolan serta pemberian contoh secara langsung.',
     'Merenungkan pencapaian atau tantangan pribadi melalui percakapan atau obrolan dengan diri sendiri.',
     'Menulis jurnal atau refleksi tentang pengalaman yang berkesan.',
     'Mengabadikan dan mengulangi foto atau video acara yang berkesan.'
     )
)

if question_15 == 'Mengabadikan dan mengulangi foto atau video acara yang berkesan.':
    question_15 = 'V'
    visual = visual + 1
elif question_15 == 'Merenungkan pencapaian atau tantangan pribadi melalui percakapan atau obrolan dengan diri sendiri.':
    question_15 = 'A'
    auditory = auditory + 1
elif question_15 == 'Menulis jurnal atau refleksi tentang pengalaman yang berkesan.':
    question_15 = 'R/W'
    readwrite = readwrite + 1
elif question_15 == 'Berdiskusi atau berbagi pengalaman berkesan melalui obrolan serta pemberian contoh secara langsung.':
    question_15 = 'K'
    kinesthetic = kinesthetic + 1
else:
    visual = 0
    auditory = 0
    readwrite = 0
    kinesthetic = 0

st.divider()

question_16 = st.radio('Bagaimana preferensi anak anda dalam kehidupan sekolah atau dirumah sehari-hari dalam hal kegiatan belajar?',
    ('',
     'Melalui presentasi secara visual atau alat bantu visual yang digunakan oleh guru.',
     'Melalui partisipasi aktif dalam diskusi kelas dan mendengarkan penjelasan guru.',
     'Melalui tugas membaca dan menulis, seperti buku teks, LKS, atau mencatat selama sesi belajar mengajar.',
     'Melalui aktivitas langsung dan keterlibatan fisik, seperti eksperimen, proyek, atau latihan bermain peran.'
     )
)

if question_16 == 'Melalui presentasi secara visual atau alat bantu visual yang digunakan oleh guru.':
    question_16 = 'V'
    visual = visual + 1
elif question_16 == 'Melalui partisipasi aktif dalam diskusi kelas dan mendengarkan penjelasan guru.':
    question_16 = 'A'
    auditory = auditory + 1
elif question_16 == 'Melalui tugas membaca dan menulis, seperti buku teks, LKS, atau mencatat selama sesi belajar mengajar.':
    question_16 = 'R/W'
    readwrite = readwrite + 1
elif question_16 == 'Melalui aktivitas langsung dan keterlibatan fisik, seperti eksperimen, proyek, atau latihan bermain peran.':
    question_16 = 'K'
    kinesthetic = kinesthetic + 1
else:
    visual = 0
    auditory = 0
    readwrite = 0
    kinesthetic = 0

#st.text(visual)
#st.text(auditory)
#st.text(readwrite)
#st.text(kinesthetic)

if "vis" not in st.session_state:
    st.session_state["vis"] = 0

if "aud" not in st.session_state:
    st.session_state["aud"] = 0

if "readW" not in st.session_state:
    st.session_state["readW"] = 0

if "kines" not in st.session_state:
    st.session_state["kines"] = 0

#############################################################################################

#############################################################################################

submit = st.button("Kirim Jawaban")
if submit:
    st.session_state["vis"] = visual
    st.session_state["aud"] = auditory
    st.session_state["readW"] = readwrite
    st.session_state["kines"] = kinesthetic
    st.session_state["pred_result"] = "available"
    st.write("Jawaban kamu telah disubmit, silahkan melihat halaman hasil untuk mengetahui detailnya")