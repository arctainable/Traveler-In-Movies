<template>
  <div>
		<section>
			<div class="container">
				<div class="project-head">
					<div class="head-info">
						<div class="row">
							<div class="col-md-4">
                <a :href="movie.poster_path" target="_blank">
                <img class="projectimg" :src="movie.poster_path" style="width:300px;">
                
                </a>
							</div>
							<div class="col-md-8">
								<div class="fundding-info" v-bind="movie">
									<div class="item-moneybar"></div>
									<div class="fundding-amount mt10">
                    <h1 class="">{{movie.title}}</h1>
                    <span class="fundding-stat">개봉중</span>
                  </div>
									<div class="mt40">
										<span class="info-text">평점</span> 
                    <br>
										<span class="info-now mr5">{{ movie.vote_avg }}/10</span> 
                    <br>
										<span class="info-goal">{{ movie.vote_count }} Ratings</span>
									</div>
									<div class="mt20">
										<span class="info-text">줄거리</span> 
                    <br>
										<span class="info-now mr5">{{ movie.overview}}</span> 
										<br>
                    <span class="info-goal">2021.11.25종료</span>
									</div>
									<div class="mt40 btn-warp">
										<button type="button" class="like-btn"><i class="fas fa-heart"></i> 121</button>
										<a class="massege-btn" href="">찜하기</a>
										<a class="share-btn" href="">공유하기</a>
									</div>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
		</section>
		<section>
			<div class="project-bar">
			</div>
		</section>
    <section class="content-section">
      <div class="container">
        <div class="row">
          <div class="col-md-8">
            <!-- 리뷰 목록 -->
            <div id="project-content" class="project-content mt40">
              <div class="community-card">
                <div class="community-card-head">
                  <span>
                    <img class="user-photo" src="../../assets/user-account.png" >
                  </span>
                  <div class="commu-write">
                    <span class="commu-writer">제목: {{review.title}}</span><br/>
                    <span class="commu-writedate">작성일: {{review.created_at.substr(0,10)}} / {{review.created_at.substr(11,8)}}</span>
                    <br>
                    <span class="commu-rank">평점: {{review.rank}}%</span>

                  </div>
                </div>
                <div class="community-card-body-review">
                  <div class="commu-content" v-html="review.content">
                  </div>
                  <div class="gmflrp"></div>
                </div>
              </div>
              <div class="community-card-foot mt10">
                <i class="fas fa-comment"></i>&nbsp;55
              </div>
            </div>
            <div>
              <router-link :to="{ name: 'Moviereviewsupdate', params: { movie_pk:movie.id } }" >
                <button>수정하기</button>
              </router-link>
              <button @click="deleted()" >삭제하기</button>
              <router-link :to="{ name: 'Moviedetail', params: { movie_pk:movie.id } }" >
                <button>리뷰목록</button>
              </router-link>
            </div>
            <!--  -->
          </div>
          <div class="col-md-4">
            <div class="writer-info mt40">
              <div class="writer-card">
                <div class="hello"></div>
                <div class="mt10"><img class="user-photo" src="../../assets/user-account.png" >감독</div>
                <div class="mt10">
                  <p>소개글 입니다~~~</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import axios from 'axios'
import {mapActions, mapGetters, mapState} from 'vuex'

export default {
  name: 'Moviereview',
  data: function () {
    return {
      movie: null,
      username: '',
      review: null,
      pageall: null,
    }
  },
  props: {
    movie_pk: {
      type: Number,
    },
    review_pk: {
      type: Number,
    }
  },
  methods: {
    ...mapActions([
      'userRankpointUpdate',
      'getReviewsGenre',
      'getReviewsCountry',
      'getReviews',
      'getReviewsMovieInfo',
      'getReviewsMovieGenreCountry',
		]),
    linkGen(pageNum) {
      return pageNum === 1 ? '?' : `?page_num=${pageNum}`
    },
    deleted: function () {
      let token = localStorage.getItem('jwt')
      let tokenHeader = {}
      if (token) {
        tokenHeader['Authorization'] = `JWT ${token}`
        this.isLogin = true
      } else {
        this.isLogin = false
      }
      let url = 'http://127.0.0.1:8000/movies/' + this.movie_pk + '/reviews/' + this.review_pk +'/'
      axios({
        method: 'delete',
        url: url,
        headers: tokenHeader,
      })  
      .then(res => {
        console.log(res.data.length),
        this.review = res.data
        const formData = new FormData()
          formData.append('rank_point', this.rank_point-10)
          formData.append('username', localStorage.getItem('username'))
          this.userRankpointUpdate(formData)
          this.getReviewsGenre()
          this.getReviewsCountry()
          this.getReviews()
          this.getReviewsMovieInfo()
          this.getReviewsMovieGenreCountry()

          Swal.fire({
            position: 'top-end',
            icon: 'info',
            title: 'Point (-10)!!',
            showConfirmButton: false,
            timer: 1500
          })
        this.$router.push({ name: 'Moviedetail' })
      })
      .catch(err => {
        console.log(err)
      })
   },
  },
  created: function () {
    let token = localStorage.getItem('jwt')
    let tokenHeader = {}
    const currentUser = localStorage.getItem("username");
    console.log(currentUser)
    if (token) {
      tokenHeader['Authorization'] = `JWT ${token}`
      this.isLogin = true
    } else {
      this.isLogin = false
    }
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/movies/' + this.movie_pk,
      headers: tokenHeader, currentUser
    })
      .then(res => {
        console.log(res.data)
        this.movie = res.data
        this.username = currentUser
      })
      .catch(err => {
        console.log(err)
      })
    let url = 'http://127.0.0.1:8000/movies/' + this.movie_pk + '/reviews/' + this.review_pk +'/'
    axios({
      method: 'get',
      url: url,
      headers: tokenHeader,
    })
      .then(res => {
        console.log(res.data.length),
        this.review = res.data
      })
      .catch(err => {
        console.log(err)
      })
  },
  watch: {
    $route() {
        let token = localStorage.getItem('jwt')
        let tokenHeader = {}
        if (token) {
          tokenHeader['Authorization'] = `JWT ${token}`
          this.isLogin = true
        } else {
          this.isLogin = false
        }
      let url = 'http://127.0.0.1:8000/movies/' + this.movie_pk + '/reviews/' + this.review_pk +'/'
      axios({
        method: 'get',
        url: url,
        headers: tokenHeader,
      })
        .then(res => {
          console.log(res.data.length),
          this.review = res.data
        })
        .catch(err => {
          console.log(err)
        })
    }
  },
  computed: {
    ...mapGetters([
      'getusernamei', 
    ]),
    ...mapState([
      'rank_point',
    ])
  },
}
</script>

<style scoped>
.community-card-body-review {
    min-height: 30px;
}
.funding-amount {
  font-family: "Black Han Sans", sans-serif;
}
</style>

