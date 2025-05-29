//SLIDE POPULER PENJUALAN

document.addEventListener('DOMContentLoaded', function () {
    const slidesWrapper = document.querySelector('.slides-wrapper');
    const slides = document.querySelectorAll('.slide');
    const prevButton = document.querySelector('.prev');
    const nextButton = document.querySelector('.next');
    const indicators = document.querySelectorAll('.indicator');

    let currentIndex = 0;
    const slideCount = slides.length;
    let autoSlideInterval;

    // Fungsi untuk memperbarui posisi slide
    function updateSlide() {
        slidesWrapper.style.transform = `translateX(-${currentIndex * 100}%)`;

        // Update indikator aktif
        indicators.forEach((indicator, index) => {
            if (index === currentIndex) {
                indicator.classList.add('active');
            } else {
                indicator.classList.remove('active');
            }
        });
    }

    // Fungsi untuk menggeser slide ke indeks berikutnya
    function nextSlide() {
        currentIndex = (currentIndex + 1) % slideCount;
        updateSlide();
    }

    // Fungsi untuk menggeser slide ke indeks sebelumnya
    function prevSlide() {
        currentIndex = (currentIndex - 1 + slideCount) % slideCount;
        updateSlide();
    }

    // Mengatur otomatis slide setiap 5 detik
    function startAutoSlide() {
        autoSlideInterval = setInterval(nextSlide, 10000);
    }

    // Menghentikan otomatis slide saat mouse hover
    function stopAutoSlide() {
        clearInterval(autoSlideInterval);
    }

    // Menambahkan event listener untuk tombol navigasi
    prevButton.addEventListener('click', function () {
        prevSlide();
        stopAutoSlide();
        startAutoSlide(); // Restart timer setelah interaksi manual
    });

    nextButton.addEventListener('click', function () {
        nextSlide();
        stopAutoSlide();
        startAutoSlide(); // Restart timer setelah interaksi manual
    });

    // Menambahkan event listener untuk setiap indikator
    indicators.forEach(indicator => {
        indicator.addEventListener('click', function () {
            currentIndex = parseInt(this.getAttribute('data-index'));
            updateSlide();
            stopAutoSlide();
            startAutoSlide(); // Restart timer setelah interaksi manual
        });
    });

    // Menghentikan slide otomatis saat mouse berada di atas slider
    document.querySelector('.slider-container').addEventListener('mouseenter', stopAutoSlide);
    document.querySelector('.slider-container').addEventListener('mouseleave', startAutoSlide);

    // Mulai slide otomatis saat halaman dimuat
    startAutoSlide();

    // Tambahkan dukungan untuk gestur swipe di mobile
    let touchStartX = 0;
    let touchEndX = 0;

    slidesWrapper.addEventListener('touchstart', function (e) {
        touchStartX = e.changedTouches[0].screenX;
        stopAutoSlide();
    }, false);

    slidesWrapper.addEventListener('touchend', function (e) {
        touchEndX = e.changedTouches[0].screenX;
        handleSwipe();
        startAutoSlide();
    }, false);

    function handleSwipe() {
        if (touchEndX < touchStartX - 50) {
            // Swipe kiri (selanjutnya)
            nextSlide();
        } else if (touchEndX > touchStartX + 50) {
            // Swipe kanan (sebelumnya)
            prevSlide();
        }
    }
});




//UNTUK TESTIMONII

document.addEventListener('DOMContentLoaded', function () {
    const track = document.querySelector('.testimonial-track');
    const cards = document.querySelectorAll('.testimonial-card');
    const dots = document.querySelectorAll('.dot');
    const prevButton = document.querySelector('.prev-button');
    const nextButton = document.querySelector('.next-button');

    let currentIndex = 0;
    const cardCount = cards.length;

    // Set up initial state
    updateCarousel();

    // Event listeners
    prevButton.addEventListener('click', function () {
        currentIndex = (currentIndex - 1 + cardCount) % cardCount;
        updateCarousel();
    });

    nextButton.addEventListener('click', function () {
        currentIndex = (currentIndex + 1) % cardCount;
        updateCarousel();
    });

    dots.forEach((dot, index) => {
        dot.addEventListener('click', function () {
            currentIndex = index;
            updateCarousel();
        });
    });

    // Auto slide every 5 seconds
    let interval = setInterval(() => {
        currentIndex = (currentIndex + 1) % cardCount;
        updateCarousel();
    }, 5000);

    // Pause auto slide on hover
    const carousel = document.querySelector('.testimonial-carousel');
    carousel.addEventListener('mouseenter', () => {
        clearInterval(interval);
    });

    carousel.addEventListener('mouseleave', () => {
        interval = setInterval(() => {
            currentIndex = (currentIndex + 1) % cardCount;
            updateCarousel();
        }, 5000);
    });

    // Touch events for mobile swipe
    let touchStartX = 0;
    let touchEndX = 0;

    carousel.addEventListener('touchstart', e => {
        touchStartX = e.changedTouches[0].screenX;
    });

    carousel.addEventListener('touchend', e => {
        touchEndX = e.changedTouches[0].screenX;
        handleSwipe();
    });

    function handleSwipe() {
        const swipeThreshold = 50;
        if (touchEndX < touchStartX - swipeThreshold) {
            // Swipe left
            currentIndex = (currentIndex + 1) % cardCount;
            updateCarousel();
        } else if (touchEndX > touchStartX + swipeThreshold) {
            // Swipe right
            currentIndex = (currentIndex - 1 + cardCount) % cardCount;
            updateCarousel();
        }
    }

    // Update carousel state
    function updateCarousel() {
        // Update track position
        track.style.transform = `translateX(${-currentIndex * 100}%)`;

        // Update dots
        dots.forEach((dot, index) => {
            dot.classList.toggle('active', index === currentIndex);
        });
    }
});

//FAQ SECTION
const questions = document.querySelectorAll('.faq-question');

    questions.forEach(q => {
      q.addEventListener('click', () => {
        const answer = q.nextElementSibling;
        const isOpen = answer.classList.contains('open');

        // Close all
        document.querySelectorAll('.faq-answer').forEach(a => a.classList.remove('open'));
        document.querySelectorAll('.faq-question').forEach(q => q.classList.remove('active'));

        // Toggle current
        if (!isOpen) {
          answer.classList.add('open');
          q.classList.add('active');
        }
      });
    });

//TIMELEINE SEJARAH

 // Mengecek elemen timeline saat discroll
 function checkAnimation() {
    const timelineItems = document.querySelectorAll('.timeline-item');
    
    timelineItems.forEach(item => {
        // Posisi item relatif terhadap viewport
        const position = item.getBoundingClientRect();
        
        // Jika item sudah memasuki viewport
        if(position.top <= window.innerHeight * 0.9) {
            item.classList.add('animate');
        }
    });
}

// Menjalankan animasi untuk item yang sudah terlihat saat halaman dimuat
window.addEventListener('load', checkAnimation);

// Menjalankan fungsi saat scroll
window.addEventListener('scroll', checkAnimation);

//UNTUK BERITA DAN ACARA

// Script untuk menambahkan komentar baru
document.getElementById('commentForm').addEventListener('submit', function(e) {
    e.preventDefault();
    
    // Mendapatkan nilai input
    const name = document.getElementById('name').value;
    const comment = document.getElementById('comment').value;
    
    // Mendapatkan tanggal saat ini
    const now = new Date();
    const formattedDate = now.toLocaleString('id-ID', {
        day: 'numeric',
        month: 'long',
        year: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
    });
    
    // Membuat elemen komentar baru
    const newComment = document.createElement('div');
    newComment.className = 'comment';
    newComment.innerHTML = `
        <div class="comment-header">
            <span class="comment-author">${name}</span>
            <span class="comment-date">${formattedDate}</span>
        </div>
        <div class="comment-body">
            <p>${comment}</p>
        </div>
    `;
    
    // Menambahkan komentar ke awal daftar
    const commentsList = document.querySelector('.comments-list');
    commentsList.insertBefore(newComment, commentsList.firstChild);
    
    // Mengupdate jumlah komentar
    const commentCountElement = document.querySelector('.comment-count');
    const currentCount = parseInt(commentCountElement.textContent);
    commentCountElement.textContent = `${currentCount + 1} Komentar`;
    
    // Reset form
    document.getElementById('commentForm').reset();
});




//DESKRIPSI PRODUK

// Script sederhana untuk tab dan counter
document.addEventListener('DOMContentLoaded', function() {
    
    
    // Quantity counter
    const minus = document.getElementById('minus');
    const plus = document.getElementById('plus');
    const input = document.querySelector('.pdp-quantity-selector input');
    
    minus.addEventListener('click', function() {
        let value = parseInt(input.value);
        if (value > 1) {
            input.value = value - 1;
        }
    });
    
    plus.addEventListener('click', function() {
        let value = parseInt(input.value);
        input.value = value + 1;
    });
});

//Penilaian Produk

// Preview foto produk
const fotoInput = document.getElementById('foto-produk');
const fotoPreview = document.getElementById('foto-preview');

fotoInput.addEventListener('change', function() {
    const file = this.files[0];
    if (file) {
        const reader = new FileReader();
        
        reader.addEventListener('load', function() {
            fotoPreview.style.backgroundImage = `url(${reader.result})`;
            fotoPreview.innerHTML = '';
        });
        
        reader.readAsDataURL(file);
    }
});

function hitungNilai() {
    // Mengambil nilai dari form
    const namaProduk = document.getElementById('nama-produk').value;
    const kategori = document.getElementById('kategori').value;
    const kelebihan = document.getElementById('kelebihan').value;
    const kekurangan = document.getElementById('kekurangan').value;
    const saran = document.getElementById('saran').value;
    const penilai = document.getElementById('penilai').value;
    
    // Mengambil nilai dari star rating
    const nilaiKualitas = document.querySelector('input[name="kualitas"]:checked')?.value || 0;
    const nilaiDesain = document.querySelector('input[name="desain"]:checked')?.value || 0;
    const nilaiFungsi = document.querySelector('input[name="fungsi"]:checked')?.value || 0;
    const nilaiKemudahan = document.querySelector('input[name="kemudahan"]:checked')?.value || 0;
    const nilaiEkonomis = document.querySelector('input[name="nilai"]:checked')?.value || 0;
    
    // Validasi form
    if (!namaProduk) {
        alert('Silakan isi nama produk!');
        return;
    }
    
    if (!kategori) {
        alert('Silakan pilih kategori produk!');
        return;
    }
    
    if (!nilaiKualitas || !nilaiDesain || !nilaiFungsi || !nilaiKemudahan || !nilaiEkonomis) {
        alert('Silakan isi semua kriteria penilaian!');
        return;
    }
    
    // Menghitung rata-rata
    const totalNilai = parseInt(nilaiKualitas) + parseInt(nilaiDesain) + parseInt(nilaiFungsi) + parseInt(nilaiKemudahan) + parseInt(nilaiEkonomis);
    const rataRata = totalNilai / 5;
    
    // Menentukan peringkat
    let peringkat = '';
    let peringkatClass = '';
    
    if (rataRata >= 4.5) {
        peringkat = 'Sangat Baik (Excellent)';
        peringkatClass = 'green';
    } else if (rataRata >= 3.5) {
        peringkat = 'Baik (Good)';
        peringkatClass = 'light-green';
    } else if (rataRata >= 2.5) {
        peringkat = 'Cukup (Average)';
        peringkatClass = 'yellow';
    } else if (rataRata >= 1.5) {
        peringkat = 'Kurang (Below Average)';
        peringkatClass = 'orange';
    } else {
        peringkat = 'Buruk (Poor)';
        peringkatClass = 'red';
    }
    
    // Mendapatkan tanggal saat ini
    const today = new Date();
    const options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
    const tanggal = today.toLocaleDateString('id-ID', options);
    
    // Fungsi untuk menampilkan nilai dengan bintang
    function getStarRating(nilai) {
        const stars = '★'.repeat(parseInt(nilai)) + '☆'.repeat(5 - parseInt(nilai));
        return `${nilai} ${stars}`;
    }
    
    // Menampilkan hasil
    document.getElementById('hasil-nama-produk').textContent = namaProduk;
    document.getElementById('hasil-kategori').textContent = kategori;
    document.getElementById('hasil-kualitas').innerHTML = getStarRating(nilaiKualitas);
    document.getElementById('hasil-desain').innerHTML = getStarRating(nilaiDesain);
    document.getElementById('hasil-fungsi').innerHTML = getStarRating(nilaiFungsi);
    document.getElementById('hasil-kemudahan').innerHTML = getStarRating(nilaiKemudahan);
    document.getElementById('hasil-nilai').innerHTML = getStarRating(nilaiEkonomis);
    document.getElementById('hasil-ratarata').textContent = rataRata.toFixed(1);
    document.getElementById('hasil-peringkat').textContent = peringkat;
    document.getElementById('hasil-peringkat').className = peringkatClass;
    document.getElementById('hasil-kelebihan').textContent = kelebihan || '-';
    document.getElementById('hasil-kekurangan').textContent = kekurangan || '-';
    document.getElementById('hasil-saran').textContent = saran || '-';
    document.getElementById('hasil-penilai').textContent = penilai || 'Anonim';
    document.getElementById('hasil-tanggal').textContent = tanggal;
    
    // Menampilkan div hasil
    document.getElementById('hasilPenilaian').style.display = 'block';
    
    // Scroll ke hasil
    document.getElementById('hasilPenilaian').scrollIntoView({ behavior: 'smooth' });
}

//INDEX HERO

// Script untuk membuat pengalaman hover yang juga bekerja di perangkat sentuh
        document.addEventListener('DOMContentLoaded', function() {
            const heroContainer = document.querySelector('.hero-container');
            const imageContainer = document.querySelector('.hero-image-container');
            
            // Toggle class untuk perangkat sentuh
            imageContainer.addEventListener('touchstart', function() {
                heroContainer.classList.toggle('touch-active');
                if (heroContainer.classList.contains('touch-active')) {
                    heroContainer.querySelector('.hero-content').style.width = '50%';
                    heroContainer.querySelector('.hero-image-container').style.width = '50%';
                } else {
                    heroContainer.querySelector('.hero-content').style.width = '70%';
                    heroContainer.querySelector('.hero-image-container').style.width = '30%';
                }
            });
        });

 // LAYANAN
  document.addEventListener('DOMContentLoaded', function() {
            const sliderTrack = document.querySelector('.slider-track');
            
            // Force hardware acceleration
            sliderTrack.style.transform = 'translateZ(0)';
            
            // Handle reduced motion
            if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
                sliderTrack.style.animationDuration = '50s';
            }
            
            console.log('Slider initialized successfully');
        });