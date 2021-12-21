<template>
  <div>

		<section>
			<div class="container">
				<div class="project-head">
					<div class="head-info">
						<div class="row">
							<div class="col-md-4" style="padding-top:30px;">
                <a :href="movie.poster_path" target="_blank" style="margin-left:75px;">
                <img class="projectimg" :src="movie.poster_path" style="width:300px;">
                
                </a>
							</div>
							<div class="col-md-8">
								<div class="fundding-info" v-bind="movie">
									<div class="fundding-amount mt10">
                    <h1 class="">{{movie.title}}</h1>
                    <span class="fundding-stat"></span>
                  </div>
									<div class="mt40">
										<span class="info-text">평점</span> 
                    <br>
										<span class="info-now mr5">{{ movie.vote_avg }} / 10</span> 
                    <br>
										<span class="info-goal">{{ movie.vote_count }} Ratings</span>
									</div>
									<div class="mt20">
										<span class="info-text">줄거리</span> 
                    <br>
										<span class="info-now mr5">{{ movie.overview}}</span> 
										<br>
                    <span class="info-goal"></span>
									</div>
									<div class="mt40 btn-warp">
										<!-- <button type="button" class="like-btn"><i class="fas fa-heart"></i> 121</button>
										<a class="massege-btn" href="">찜하기</a>
										<a class="share-btn" href="">공유하기</a> -->
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
          <div class="col-md-12">
            <div class="project-content mt40">
              <div class="rmfTmrldiv">
                <div class="pull-left">
                  <img class="user-photo" v-if="profile_image === `${SERVER_URL}null`" src='@/assets/user-account.png' alt="">
                  <img class="user-photo" v-else :src="profile_image" alt="">
                  <!-- <img class="user-photo" src="../../assets/user-account.png" > -->
                  <span v-if="isLogin">{{username}}님 영화에 대한 리뷰를 작성해주세요~</span>
                  <span v-else>로그인한 유저만 글을 쓸 수 있습니다</span>
                </div>
                <div class="pull-right">
                  <router-link :to="{ name: 'Moviereviewswrite', params: { movie_pk:movie.id, username:getusernamei } }" >
                    <button type="button" class="btn btb-default" style="background:white; color:black;">글쓰기</button>
                  </router-link>
                </div>
                <div class="clearfix"></div>
              </div>
            </div>
            <!-- 리뷰 목록 -->
            <div id="project-content" class="project-content mt40" v-for="review in reviews" v-bind:key="review">
              <div class="community-card">
                <div class="community-card-head">
                  <span>
                    <!-- 여기 안됨 -->
                    <img class="user-photo" v-if="review.user.profile_image === `${SERVER_URL}null`" src='@/assets/user-account.png' alt="">
                    <img class="user-photo" v-else :src="`${SERVER_URL}`+review.user.profile_image" alt="">
                  </span>
                  <div class="commu-write">
                    <span class="commu-writer">제목: {{review.profile_image}} {{review.title}}</span><br/>
                    <span class="commu-writedate">작성일: <span class="commu-writedate">작성일: {{review.created_at.substr(0,10)}} / {{review.created_at.substr(11,8)}}</span></span>
                    <br>
                    <span class="commu-rank">평점: {{review.rank}}%</span>

                  </div>
                </div>
                <div class="community-card-body">
                  <div class="commu-content" v-html="review.content">
                  </div>
                </div>
              </div>
              <div class="more-content mt20">
                <router-link :to="{ name: 'Moviereviews', params: { movie_pk:movie.id, username:getusernamei, review_pk: review.id} }" 
                style="color:white; text-decoration: none;">더 보기</router-link>
              </div>
              <div class="community-card-foot mt10">
                <i class="fas fa-comment"></i>&nbsp;{{review.comments_count}}
              </div>
            </div>
            <div>
              <div class="overflow-auto">
                <b-pagination-nav :link-gen="linkGen" :number-of-pages="pageall.total_pages" align="center" use-router></b-pagination-nav>
              </div>
            </div>
            <!--  -->
          </div>

        </div>
      </div>
    </section>
  </div>
</template>

<script>
import axios from 'axios'
import {mapState, mapGetters} from 'vuex'
import SERVER from '@/api/server.js'


export default {
  name: 'Moviedetail',
  data: function () {
    return {
      SERVER_URL: SERVER.URL,
      movie: null,
      username: '',
      reviews: null,
      pageall: null,
      commentlength: null,
    }
  },
  props: {
    movie_pk: {
      type: String,
    }
  },
  methods: {
      linkGen(pageNum) {
        return pageNum === 1 ? '?' : `?page_num=${pageNum}`
      }
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
    let url = 'http://127.0.0.1:8000/movies/' + this.movie_pk + '/reviews/'
    if (this.$route.query.page_num) {
      url += '?page_num=' + this.$route.query.page_num
    }
    axios({
      method: 'get',
      url: url,
      headers: tokenHeader,
    })
      .then(res => {
        console.log(res.data.length),
        this.pageall = res.data[res.data.length - 1],
        res.data.pop(),
       res.data[0].content = res.data[0].content.substring(0, 50)
        this.reviews = res.data
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
      let url = 'http://127.0.0.1:8000/movies/' + this.movie_pk + '/reviews/'
      if (this.$route.query.page_num) {
        url += '?page_num=' + this.$route.query.page_num
      }
      axios({
        method: 'get',
        url: url,
        headers: tokenHeader,
      })
        .then(res => {
          console.log(res.data.length),
          this.pageall = res.data[res.data.length - 1],
          res.data.pop(),
          this.reviews = res.data
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
      'profile_image',
    ]),
  },
    
}
</script>
<style scoped>
.funding-amount {
  font-family: "Black Han Sans", sans-serif;
}
.content-section {
  min-height: 350px;
}
</style>