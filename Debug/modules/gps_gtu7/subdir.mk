################################################################################
# Automatically-generated file. Do not edit!
# Toolchain: GNU Tools for STM32 (12.3.rel1)
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
C:/Users/Sheen/Desktop/Embedded_System/I2C_tmphm/i2c-class-1-code-master/modules/gps_gtu7/gps_gtu7.c 

OBJS += \
./modules/gps_gtu7/gps_gtu7.o 

C_DEPS += \
./modules/gps_gtu7/gps_gtu7.d 


# Each subdirectory must supply rules for building sources it contributes
modules/gps_gtu7/gps_gtu7.o: C:/Users/Sheen/Desktop/Embedded_System/I2C_tmphm/i2c-class-1-code-master/modules/gps_gtu7/gps_gtu7.c modules/gps_gtu7/subdir.mk
	arm-none-eabi-gcc "$<" -mcpu=cortex-m4 -std=gnu11 -g3 -DDEBUG -DSTM32F401xE -DUSE_FULL_LL_DRIVER -DHSE_VALUE=8000000 -DHSE_STARTUP_TIMEOUT=100 -DLSE_STARTUP_TIMEOUT=5000 -DLSE_VALUE=32768 -DEXTERNAL_CLOCK_VALUE=12288000 -DHSI_VALUE=16000000 -DLSI_VALUE=32000 -DVDD_VALUE=3300 -DPREFETCH_ENABLE=1 -DINSTRUCTION_CACHE_ENABLE=1 -DDATA_CACHE_ENABLE=1 -c -I../Core/Inc -I../Drivers/STM32F4xx_HAL_Driver/Inc -I../Drivers/CMSIS/Device/ST/STM32F4xx/Include -I../Drivers/CMSIS/Include -I"C:/Users/Sheen/Desktop/Embedded_System/I2C_tmphm/i2c-class-1-code-master/modules/include" -O0 -ffunction-sections -fdata-sections -Wall -fstack-usage -fcyclomatic-complexity -MMD -MP -MF"$(@:%.o=%.d)" -MT"$@" --specs=nano.specs -mfpu=fpv4-sp-d16 -mfloat-abi=hard -mthumb -o "$@"

clean: clean-modules-2f-gps_gtu7

clean-modules-2f-gps_gtu7:
	-$(RM) ./modules/gps_gtu7/gps_gtu7.cyclo ./modules/gps_gtu7/gps_gtu7.d ./modules/gps_gtu7/gps_gtu7.o ./modules/gps_gtu7/gps_gtu7.su

.PHONY: clean-modules-2f-gps_gtu7

