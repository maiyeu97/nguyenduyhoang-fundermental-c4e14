# Lưu ý: Nếu bạn chưa cài đặt youtube-dl, hãy thực hiện nó trước khi thử hướng dẫn này
# Mở lệnh lline (Ctrl + `) rồi nhập:
# pip cài đặt youtube-dl
từ youtube_dl import YoutubeDL

# Gõ và chạy các mẫu dưới đây, từng cái một
# Kết quả: https://www.dropbox.com/s/cm5m6zitnuwdqbk/Screenshot%202017-12-08%2005.32.02.png?dl=0

# Mẫu 1: Tải xuống một video youtube
dl = YoutubeDL ()
dl.download ([ ' https://www.youtube.com/watch?v=WHK5p7JL7g4 ' ]) # Hãy nhớ đặt video của bạn vào danh sách, mặc dù một video đã được tải xuống



# Mẫu 2: Tải xuống nhiều video trên YouTube
dl = YoutubeDL ()
# Đưa danh sách các url bài hát vào chức năng tải xuống để tải chúng, từng cái một
dl.download ([ ' https://www.youtube.com/watch?v=wNVIn-QS4DE ' , ' https://www.youtube.com/watch?v=JZjRrg2rpic ' ])



# Mẫu 3: Tải xuống âm thanh
options = {
    ' format ' : ' bestaudio / audio '  # Nói với người downloader chỉ tải về chất lượng âm thanh tốt nhất
}
dl = YoutubeDL (tùy chọn)
dl.download ([ ' https://www.youtube.com/watch?v=JZjRrg2rpic ' ])



# Mẫu 4: Tìm kiếm và sau đó tải xuống video đầu tiên
options = {
    ' default_search ' : ' ytsearch ' , # tell downloader để tìm kiếm thay vì tải trực tiếp
    ' max_downloads ' : 1  # Nói với người downloader chỉ tải về mục nhập đầu tiên (video)
}
dl = YoutubeDL (tùy chọn)
dl.download ([ ' con điên TAMKA PKL ' ))


# Mẫu 5: Tìm kiếm và sau đó tải xuống âm thanh đầu tiên
options = {
    ' default_search ' : ' ytsearch ' , # tell downloader để tìm kiếm thay vì tải trực tiếp
    ' max_downloads ' : 1 , # Tell downloader chỉ tải về mục nhập đầu tiên (audio)
    ' định dạng ' : ' bestaudio / audio '
}
dl = YoutubeDL (tùy chọn)
dl.download ([ ' Nhớ mưa sài gòn trường ' ])
