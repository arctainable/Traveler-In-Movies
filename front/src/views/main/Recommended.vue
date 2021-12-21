<template>
  <div id='Recommended'>
    <h1>이건 레코멘디드</h1>
    <!-- bg you/tube 영상이 클릭되지 않게 투명 벽 생성 -->
    <div id='wall' style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; opacity: 0;"></div>

    <!-- autoplay / fullscreen / prevent touch / autoplay=1&mute=1 -> autoplay ex&chrome--> <!-- {{ videoUrl }} -->
    <iframe width="1920" height="1080" :src="newVid" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

    <!-- carousel poster -->
    <div id="carousel" style="opacity: 0.8;">
      <carousel-3d :width="180" :height="250" :display="9" :autoplay="false" @click="nextCard()">
        <slide v-for="(movie, i) in movies" :key="i" :index="i" class="contentContainer">
            <img :src="movie.poster_path" @click="[changeBGVideo(i)]" style="height: 100%; width: 100%;">
            <div class="overlay" @click="[changeBGVideo(i)]">
              <div class="textIncard" style="width=100%; height=100%;">
                <br><br> 
                <p style="white-space: nowrap; font-weight: bold;">{{movie.title}}</p>
                <b-icon icon="badge-tm-fill" font-scale="1"></b-icon> Rate : {{ movie.vote_avg * 10 }}%<br><br> 
                <b-icon icon="geo-alt" animation="cylon" font-scale="1" variant="success"></b-icon>  : {{ movie.country_name }}<br><br> 
                <b-button pill size="sm" @click="[showCard(i), getDirector()]">크게 보기</b-button>
                </div>
            </div>
        </slide>
      </carousel-3d>
    </div>
    
    <!-- card -->
    <div class="container" v-show="card_clicked">
        <div class="row col-12">
            <div style="justify-content: center; align-items: center;">
                <div class="card card-flip h-100">
                    <!-- card front -->
                    <div class="card-front text-white bg-dark">
                      <img :src="movies[this.cardIdx].poster_path" alt="" style="width: 300px; height: 100%; display: flex;" class="card-body col-sm-4">
                      <div class="card-body col-sm-7" style="display: flex;">
                        <div class="col" style="font-family: 'Do Hyeon', sans-serif; font-size: 30px; padding:1.5rem;">
                          <p class="card-title row-sm-3" style="font-family: 'Black Han Sans', sans-serif; font-size: 45px">{{movies[this.cardIdx].title}}</p>
                          <!-- img table -->
                          <table class="table table-dark" style="font-size: 20px;" fixed="fixed">
                          <tbody class="row-sm-2">
                            <td>
                              <tr><div v-if="movies[this.cardIdx].director_path"><b-avatar :src="movies[this.cardIdx].director_path" size="8rem"></b-avatar></div>
                                <div v-else><b-avatar avatar icon="people-fill"></b-avatar></div>
                              </tr>
                              <tr>{{movies[this.cardIdx].director_name}}</tr>
                              <tr>감독</tr>
                            </td>
                            <td>
                              <tr><div v-if="movies[this.cardIdx].actor1_path"><b-avatar :src="movies[this.cardIdx].actor1_path" size="8rem"></b-avatar></div>
                                <div v-else><b-avatar avatar icon="people-fill" size="8rem"></b-avatar></div>
                              </tr>
                              <tr v-if="movies[this.cardIdx].actor1_name">{{movies[this.cardIdx].actor1_name}}</tr>
                              <tr v-if="movies[this.cardIdx].actor1_name">주연</tr>
                              <tr v-if="!movies[this.cardIdx].actor1_name">앗, 배우 정보가</tr>
                              <tr v-if="!movies[this.cardIdx].actor1_name"> 없네요 😫</tr>
                            </td>
                            <td>
                              <tr><div v-if="movies[this.cardIdx].actor2_path"><b-avatar :src="movies[this.cardIdx].actor2_path" size="8rem"></b-avatar></div>
                                <div v-else><b-avatar avatar icon="people-fill" size="8rem"></b-avatar></div>
                              </tr>
                              <tr v-if="movies[this.cardIdx].actor2_name">{{movies[this.cardIdx].actor2_name}}</tr>
                              <tr v-if="movies[this.cardIdx].actor2_name">주연</tr>
                              <tr v-if="!movies[this.cardIdx].actor2_name">앗, 배우 정보가</tr>
                              <tr v-if="!movies[this.cardIdx].actor2_name"> 없네요 😫</tr>
                            </td>
                          </tbody>
                          <tbody class="row-sm-2">
                            <td>
                              <br>
                              <tr><div v-if="movies[this.cardIdx].actor3_path"><b-avatar :src="movies[this.cardIdx].actor3_path" size="8rem"></b-avatar></div>
                                <div v-else><b-avatar avatar icon="people-fill" size="8rem"></b-avatar></div>
                              </tr>
                              <tr v-if="movies[this.cardIdx].actor3_name">{{movies[this.cardIdx].actor3_name}}</tr>
                              <tr v-if="movies[this.cardIdx].actor3_name">조연</tr>
                              <tr v-if="!movies[this.cardIdx].actor3_name">앗, 배우 정보가</tr>
                              <tr v-if="!movies[this.cardIdx].actor3_name"> 없네요 😫</tr>
                            </td>
                            <td>
                              <br>
                              <tr><div v-if="movies[this.cardIdx].actor4_path"><b-avatar :src="movies[this.cardIdx].actor4_path" size="8rem"></b-avatar></div>
                                <div v-else><b-avatar avatar icon="people-fill" size="8rem"></b-avatar></div>
                              </tr>
                              <tr v-if="movies[this.cardIdx].actor4_name">{{movies[this.cardIdx].actor4_name}}</tr>
                              <tr v-if="movies[this.cardIdx].actor4_name">조연</tr>
                              <tr v-if="!movies[this.cardIdx].actor4_name">앗, 배우 정보가</tr>
                              <tr v-if="!movies[this.cardIdx].actor4_name"> 없네요 😫</tr>
                            </td>
                            <td>
                              <br>
                              <tr><div v-if="movies[this.cardIdx].actor5_path"><b-avatar :src="movies[this.cardIdx].actor5_path" size="8rem"></b-avatar></div>
                                <div v-else><b-avatar avatar icon="people-fill" size="8rem"></b-avatar></div>
                              </tr>
                              <tr v-if="movies[this.cardIdx].actor5_name">{{movies[this.cardIdx].actor5_name}}</tr>
                              <tr v-if="movies[this.cardIdx].actor5_name">조연</tr>
                              <tr v-if="!movies[this.cardIdx].actor5_name">앗, 배우 정보가</tr>
                              <tr v-if="!movies[this.cardIdx].actor5_name"> 없네요 😫</tr>
                            </td>
                          </tbody>
                          </table>
                        </div>
                      </div>
                    </div>
                    <!-- card back -->
                    <div class="card-back text-white bg-dark">
                          <div class="card-title col-sm-5">
                            <p class="card-title row-sm-3" style="font-family: 'Black Han Sans', sans-serif; font-size: 40px; white-space: nowrap;">{{movies[this.cardIdx].title}}</p><br>
                            <p class="row-sm-2" style="font-size:25px;"><b-icon icon="badge-tm-fill"></b-icon> Rate : {{ movies[this.cardIdx].vote_avg * 10 }}%</p>
                            <p class="row-sm-2" style="font-size:25px;"><b-icon icon="geo-alt" animation="" font-scale="1" variant="success"></b-icon>  : {{ movies[this.cardIdx].country_name }}</p>
                            <p class="row-sm-2" style="font-size:25px;"><b-icon icon="tags"></b-icon> : 
                            <span v-for="(genre, idx) in genres[this.cardIdx]" :key="idx">
                              <span>{{genre.name}} | </span>
                            </span> 
                            </p>
                            <span class="card-dark">{{movies[this.cardIdx].overview.substr(0,250)}}...</span>
                          </div>
                          <b-icon icon="x" animation="" variant="danger" font-scale="3" @click="showCard(cardIdx)" style="position:fixed; bottom:0; font-size:3rem"></b-icon>
                              <b-button size="sm" class="mb-2" @click="showCard(cardIdx)" style="position:fixed; bottom:0; left:3rem; margin-bottom:0.5rem; opacity:0.7;">
                                <router-link style="text-decoration: none; color: inherit;" :to="{ name: 'Moviedetail', params: { movie_pk:movies[cardIdx].id } }"><b-icon icon="film" aria-hidden="true"></b-icon> READ MORE</router-link>
                              </b-button>
                          <div class="card-body col-sm-7 card bg-dark" style="display: flex; width:100%; text-align:center">
                                <div class="container row-sm-3" style="padding:3rem; font-family: 'Do Hyeon', sans-serif; font-size:30px;">Best scene in the<br>'{{ movies[cardIdx].title }}'</div>
                              <img :src="movies[cardIdx].backdrop_path" alt="" v-if="movies[cardIdx].backdrop_path">
                              <div v-else class="text-align:center"><h1>앗, 대표 이미지가 없네요😫 첫 사진의 주인공이 되어볼까요?</h1></div>
                              <div id="reviews row" style="justify-content:center; align-items:center;">

                              </div>
                          </div>
                    </div>
                </div>
            </div>
        </div>
    </div>




  </div>
</template>

<script>
import { Carousel3d, Slide } from 'vue-carousel-3d';
import axios from 'axios'
import _ from 'lodash'

export default {
  name: 'Recommended',
  data: function () {
    return {
      videoUrl: null,
      movies: null,
      card_clicked: false,
      autoPlay: '&rel=0&autoplay=1&mute=1',
      hideBar: '&controls=0&&showinfo=0&modestbranding=1&autohide=1',
      cardIdx: 0,
      genres: [],
      directors: [],
      reviews: [],
    }
  },
  components: {
    Carousel3d,
    Slide,
  },
  methods: {
    getMovies: function () {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/movies/',
      })
        .then(res => {
          this.movies = _.sampleSize(res.data, 9) 
          console.log(this.movies)
        })
        .catch(err => {
          console.log(err)
        })
    },
    getGenres: function () {
      for (let i = 0; i < 9; i++) {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/movies/${this.movies[i].id}/genres`,
      })
        .then(res => {
          this.genres[i] = res.data
          // console.log(this.genres)
        })
        .catch(err => {
          console.log(err)
        })
      }
    },
    changeBGVideo: function (n) {
      // countryUrl => store로 이전 예정
      const countryUrl = {
        브라질: "https://www.youtube.com/embed/1PTs1mqrToM?start=87",
        콜롬비아: "https://www.youtube.com/embed/NHZosHEwcZQ?start=5",
        멕시코: "https://www.youtube.com/embed/QqsyIhIPng0?start=10",
        라스베이거스: "https://www.youtube.com/embed/Inun9TW-0Fo?start=10",
        워싱턴: "https://www.youtube.com/embed/Os76WrJspy0?start=74",
        시카고: "https://www.youtube.com/embed/taf4gHPae20?start=5",
        캐나다: "https://www.youtube.com/embed/ArR-ctuKraE?start=24",
        칠레: "https://www.youtube.com/embed/oJsYG5lm6Ys?start=3",
        일본: "https://www.youtube.com/embed/MaefAK3njXo?start=342",
        홍콩: "https://www.youtube.com/embed/P71I7akn7PU?start=99",
        중국: "https://www.youtube.com/embed/E9-0HRFd6sU?start=13",
        인도: "https://www.youtube.com/embed/o_24LPjOIHI?start=31",
        호주: "https://www.youtube.com/embed/pcWbYUL7Lmo?start=578",
        뉴질랜드: "https://www.youtube.com/embed/5uu0NGgGWb8?start=153",
        영국: "https://www.youtube.com/embed/gs-skMbz9vo?start=45",
        프랑스: "https://www.youtube.com/embed/3UozcMEwPMI?start=27",
        이탈리아: "https://www.youtube.com/embed/G0EUqGhYZ6Y?start=18",
        남아프리카공화국: "https://www.youtube.com/embed/WvJj_VUgzK0?start=789",
        소말리아: "https://www.youtube.com/embed/wPMH1R1iP8w?start=145",
        모로코: "https://www.youtube.com/embed/ZE81dWxNnMQ?start=172",
        }
      const target = this.movies[n].country_name
      this.videoUrl = countryUrl[target] + this.autoPlay + this.hideBar
    },
    logout: function () {
    },
    showCard: function (i) {
      this.card_clicked = !this.card_clicked
      this.cardIdx = i
    },
    nextCard: function () {
      this.card_clicked = false
    },
  },
  computed: {
    newVid: function () {
      return this.videoUrl
    }
  },
  created: function () {
    this.videoUrl = 'https://www.youtube.com/embed/vGY5sLdyajk?start=264' + this.autoPlay + this.hideBar +'&loop=1&playlist=vGY5sLdyajk'
    if (this)
    this.getMovies()
  },
  updated: function () {
    this.getGenres()
    },
  }
  
</script>

<style>
#home > iframe {
  z-index: -2;
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  opacity: 1.0;
}

#wall {
   z-index: -1;
}

#carousel {
  position: fixed;
  bottom: 0px;
  width: 100%;
  display: flex;
  justify-content: center;
}

/* hover */
/* .contentContainer {
  position: relative;
  width: 100%;
} */

.image {
  display: block;
  width: 100%;
  height: 100%;
}

.overlay {
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  height: 100%;
  width: 100%;
  opacity: 0;
  transition: .5s ease;
  background-color: black;
}

.contentContainer:hover .overlay {
  opacity: 0.9;
}

.textIncard {
  color: white;
  font-size: 15px;
  position: absolute;
  top: 50%;
  left: 50%;
  -webkit-transform: translate(-50%, -50%);
  -ms-transform: translate(-50%, -50%);
  transform: translate(-50%, -50%);
  text-align: center;
  width: 100%;
  height: 100%;
}


/* card */

.card-flip > div {
  backface-visibility: hidden;
  transition: transform 300ms;
  transition-timing-function: linear;
  width: 100%;
  height: 100%;
  margin: 0;
  display: flex;
}

.card-front {
  transform: rotateY(0deg);
}

.card-back {
  transform: rotateY(180deg);
  position: absolute;
  top: 0;
}

.card-flip:hover .card-front {
  transform: rotateY(-180deg);
}
  
.card-flip:hover .card-back {
  transform: rotateY(0deg);
}

.container {
  opacity: 0.9;
}

/* table */
.table {
  text-align: center;
}

</style>
