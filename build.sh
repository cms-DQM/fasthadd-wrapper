BUILD_ROOT=/tmp/${USER}/fasthadd
rm -rf ${BUILD_ROOT}
mkdir -p $BUILD_ROOT

cp fastHadd $BUILD_ROOT
cp hadd $BUILD_ROOT

#cd $BUILD_ROOT
rpmbuild --target x86_64 -bb fasthadd-wrapper.spec --buildroot=${BUILD_ROOT}/build --define "_topdir ${BUILD_ROOT}"
#cd -
#rm -rf ${BUILD_ROOT}
