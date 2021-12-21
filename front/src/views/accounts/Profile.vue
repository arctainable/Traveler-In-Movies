<template>
	<div id="profile_main">		
		<!-- 프로필 유저 이름, 닉네임, 랭크, 프로필 사진 등 -->
		<ProfileInfo
		class="d-block"
		/>
	</div>
</template>

<script>
// import axios from 'axios'
import ProfileInfo from '@/components/Profile/ProfileInfo'
// import {mapActions, mapGetters} from 'vuex'

export default {
	name: 'Profile',
	components: {
		ProfileInfo,
	},
	// method: {
	// 	...mapActions([
	// 	// 'loginGetToken',
  //   'getProfile',
  //   'getReviewsGenre',
  //   'getReviewsCountry',
  //   'getReviews',
  //   'getReviewsMovieInfo',
  //   'getReviewsMovieGenreCountry',
	// 	]),
	// },

	// mounted: function () {
	// 	this.getProfile()
	// 	this.getReviewsGenre()
  //   this.getReviewsCountry()
  //   this.getReviews()
  //   this.getReviewsMovieInfo()
  //   this.getReviewsMovieGenreCountry()
	// },

	// computed:  {
	// 	...mapGetters([
	// 		'getUserId'
	// 	])
	// }
}
</script>


<style>
h2 {
  color: black;
  font-weight: 200;
}
.navbar {
	border-radius: 0px;
	margin-bottom: 0px;
}


</style>