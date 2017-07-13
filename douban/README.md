This a project to collect the "ranking", "score", "movie_name" and "score_num" information about the douban_top250 movies.    

This project could output json file and xsw file as following operations.

### json file
__command line__: scrapy crawl douban_movie spider  
__important__: remember to enable the pipeline settings in the settings.py file to output douban_movie.json

### xsw file
__command line__: scrapy crawl douban_movie -o douban.csv
